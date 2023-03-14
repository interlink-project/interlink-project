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

                sh '''
                cat << EOF >> .env
                $ENV
                EOF
                '''

                sh '''
                cat << EOF >> secrets.env
                $ENV
                EOF
                '''


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
                # Apply last migrations (if they exist)
                # and seed the database (if objects already exist, initial_data.py script updates them)
                docker-compose exec -T catalogue python /app/app/pre_start.py && \
                docker-compose exec -T catalogue alembic upgrade head && \
                docker-compose exec -T catalogue ./seed.sh &
                docker-compose exec -T coproduction alembic upgrade head && \
                docker-compose exec -T coproduction ./seed.sh &

                exit

                EOF

            """
            }
          }
        }
      }


    }
}