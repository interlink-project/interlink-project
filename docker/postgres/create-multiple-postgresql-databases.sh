#!/bin/bash

set -e
set -u

# hstore extension needed for database localization https://sqlalchemy-utils.readthedocs.io/en/latest/internationalization.html

function create_user_and_database() {
	local database=$1
	echo "  Creating user and database '$database'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
		    CREATE USER $database;
		    CREATE DATABASE $database;
		    GRANT ALL PRIVILEGES ON DATABASE $database TO $database;

	EOSQL

	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL

			  CREATE ROLE viewer;
		    ALTER USER viewer PASSWORD 'viewer';
        GRANT CONNECT ON DATABASE $database TO viewer;
        GRANT USAGE ON SCHEMA public TO viewer;
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO viewer;

	EOSQL

	psql -d $database -c 'create extension hstore;'
}

if [ -n "$POSTGRES_MULTIPLE_DATABASES" ]; then
	echo "Multiple database creation requested: $POSTGRES_MULTIPLE_DATABASES"
	for db in $(echo $POSTGRES_MULTIPLE_DATABASES | tr ',' ' '); do
		create_user_and_database $db
	done
	echo "Multiple databases created"
fi
