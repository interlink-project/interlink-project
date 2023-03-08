def getEnvironmentInfo() {
    switch(env.BRANCH_NAME) {
        case "demo":
            configPath = "demo"
            secrets = [
              [path: 'demo/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = env.BRANCH_NAME
            break

        case "pilot-mef":
            configPath = "pilot-mef"
            secrets = [
              [path: 'pilot-mef/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = env.BRANCH_NAME
            break

        case "pilot-varam":
            configPath = "pilot-varam"
            secrets = [
              [path: 'pilot-varam/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = env.BRANCH_NAME
            break

        case "pilot-zgz":
            configPath = "pilot-zgz"
            secrets = [
              [path: 'pilot-zgz/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = env.BRANCH_NAME
            break

        case "master":
            configPath = "development"
            secrets = [
              [path: 'development/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = env.BRANCH_NAME
            break

        default:
            configPath = "development"
            secrets = [
              [path: 'development/secrets', engineVersion: 2, secretValues: [
                        [envVar: 'SSH_USER', vaultKey: 'ssh_user'],
                        [envVar: 'SERVER_IP', vaultKey: 'server_ip'],
                        [envVar: 'PATH', vaultKey: 'path'],
                        [envVar: 'ENV', vaultKey: 'env_file']
                    ]
                ],
            ]
            branch = 'master'
            break
    }
    return [configPath, secrets]
}





def configuration = [vaultUrl: 'http://vault:8200',  vaultCredentialId: 'vault-approle', engineVersion: 2]

(configPath, secrets) = getEnvironmentInfo()

pipeline {

    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '20'))
        disableConcurrentBuilds()
    }
    stages{



      stage('checkout') {
        steps {
          withVault([configuration: configuration, vaultSecrets: secrets]) {
            sshagent(credentials : ['id_rsa']) {
            sh """

                ssh -o StrictHostKeyChecking=no -tt ${env.SSH_USER}@${env.SERVER_IP} << EOF

                git clone https://github.com/interlink-project/interlink-project.git ${env.PATH}/interlink-project || true
                cd ${env.PATH}/interlink-project/envs/${configPath}


                git fetch --force --all --tags
                git checkout --force origin/${branch} || git checkout --force ${branch}

                git restore .env

                exit


                EOF

            """
            }
          }
        }
      }

      stage('copy env file') {
        steps {
          withVault([configuration: configuration, vaultSecrets: secrets]) {
            sshagent(credentials : ['id_rsa']) {
            sh """

                ssh -o StrictHostKeyChecking=no -tt ${env.SSH_USER}@${env.SERVER_IP} << EOF

                cd ${env.PATH}/interlink-project/envs/${configPath}

                echo "${env.ENV}" >> .env
                echo "${env.ENV}" > secrets.env


                exit


                EOF

            """
            }
          }
        }
      }

      stage('docker-compose up') {
        steps {
          withVault([configuration: configuration, vaultSecrets: secrets]) {
            sshagent(credentials : ['id_rsa']) {
            sh """

                ssh -o StrictHostKeyChecking=no -tt ${env.SSH_USER}@${env.SERVER_IP} << EOF

                cd ${env.PATH}/interlink-project/envs/${configPath}

                docker-compose pull
                docker network create traefik-public || true
                docker network create grafana-network || true
                docker-compose up -d
                sleep 10


                exit


                EOF

            """
            }
          }
        }
      }

      stage('update db') {
        steps {
          withVault([configuration: configuration, vaultSecrets: secrets]) {
            sshagent(credentials : ['id_rsa']) {
            sh """

                ssh -o StrictHostKeyChecking=no -tt ${env.SSH_USER}@${env.SERVER_IP} << EOF

                cd ${env.PATH}/interlink-project/envs/${configPath}


                sudo apt install python3-pip -y
                pip3 install python-dotenv && python3 setup-dremio.py
                docker-compose exec -T catalogue python /app/app/pre_start.py
                docker-compose exec -T coproduction python /app/app/pre_start.py
                # Apply last migrations (if they exist)
                docker-compose exec -T catalogue alembic upgrade head
                docker-compose exec -T coproduction alembic upgrade head

                # Seed the database (if objects already exist, initial_data.py script updates them)
                docker-compose exec -T catalogue ./seed.sh
                docker-compose exec -T coproduction ./seed.sh

                # Give permissions to postgres user to access the database
                docker-compose exec -T db psql -U postgres -c "CREATE ROLE viewer  with LOGIN ENCRYPTED PASSWORD 'viewer';" || true
                docker-compose exec -T db psql -U postgres -c "GRANT CONNECT ON DATABASE coproduction_production TO viewer;"
                docker-compose exec -T db psql -U postgres -c "GRANT CONNECT ON DATABASE catalogue_production TO viewer;"
                docker-compose exec -T db psql -U postgres -c "GRANT USAGE ON SCHEMA public TO viewer;"
                docker-compose exec -T db psql -U postgres -d coproduction_production -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO viewer;"
                docker-compose exec -T db psql -U postgres -d catalogue_production -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO viewer;"
                docker-compose exec -T db psql -U postgres -c "ALTER ROLE viewer WITH LOGIN;"

                exit

                EOF

            """
            }
          }
        }
      }


    }
}