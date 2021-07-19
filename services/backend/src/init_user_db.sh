#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER simha;
    CREATE DATABASE btgapp;
    GRANT ALL PRIVILEGES ON DATABASE btgapp TO simha;
EOSQL

# heredocs Linux
#
#[COMMAND] <<[-] 'DELIMITER'
#  HERE-DOCUMENT
#DELIMITER