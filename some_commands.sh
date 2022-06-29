# URL para ver las acciones
https://github.com/interlink-project/interlink-project/actions

# Hacer SSH a los servidores
ssh -i id_rsa interlink@dev.interlink-project.eu
cd /datadrive/data/interlink-project/envs

# Copiar backups a local
scp -r -i id_rsa interlink@varam.interlink-project.eu:/datadrive/data/db_backups .

# Seed de initial data (se hace en los workflows)
docker-compose exec -T catalogue ./seed.sh
docker-compose exec -T coproduction ./seed.sh

# Si loomio se desconfigura, con esto se le aplican las migraciones que necesita para iniciarse
docker-compose exec -T loomio rake db:setup 

############################################################################
# Tagear servicios
############################################################################
# ver tags existentes
git tag

# crear tag
git tag -a v1.1.4 -m "Interlinker update schema"
# o
git tag -a v1.1.4 bc1da2b01780ebece95133d575bb9b60b423cc8a -m "Interlinker update schema"

# push tag
git push origin v1.1.4

############################################################################
# Borrar los datos de las bases de datos de coproduction y catalogue
############################################################################
# Eliminar los contenedores coproduction, coproductionworker y catalogue
# Entrar a una shell del contenedor "db" (puedes hacerlo en portainer)
# Iniciamos la conexion al postgres
psql postgresql://postgres:changethis@localhost:5432

# Eliminar y crear las bds
DROP DATABASE catalogue_production;
DROP DATABASE coproduction_production;
CREATE DATABASE catalogue_production;
CREATE DATABASE coproduction_production;
exit

# Crear las extensiones HSTORE
psql postgresql://postgres:changethis@localhost:5432/coproduction_production -c 'create extension hstore;'
psql postgresql://postgres:changethis@localhost:5432/catalogue_production -c 'create extension hstore;'
