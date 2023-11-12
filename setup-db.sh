#!/bin/bash

if [ -f .env ]; then
  export $(echo $(cat .env | sed 's/#.*//g' | sed 's/\r//g' | xargs -0) | envsubst);
fi

cd ~postgres

sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "CREATE DATABASE $DB_NAME;"
sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD';"
sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "ALTER ROLE $DB_USER SET client_encoding TO 'utf8';"
sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';"
sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "ALTER ROLE $DB_USER SET timezone TO 'UTC';"
sudo PGPASSWORD=$PGPASSWORD -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;"
