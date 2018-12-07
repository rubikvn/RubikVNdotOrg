#!/bin/bash

# Script to initialize MySQL database inside the container for development

docker-compose up -d db

# Copying template files to the database container
docker cp $PWD/RubikVNdotOrg/db/my.cnf rbvn_mysql_database:/root
docker cp $PWD/RubikVNdotOrg/db/rubikvn_schema.sql rbvn_mysql_database:/root

docker-compose exec db /bin/bash -c "cat /root/my.cnf | tee -a /etc/mysql/my.cnf"
# Apply changes to config
docker-compose restart db

docker-compose exec db /bin/bash -c "mysql -e 'DROP DATABASE IF EXISTS rubikvn';"
docker-compose exec db /bin/bash -c "mysql -e 'CREATE DATABASE rubikvn;'"

sleep 1

docker-compose exec db /bin/bash -c "mysql -u root --default-character-set=utf8mb4 rubikvn < /root/rubikvn_schema.sql"

docker-compose run web python manage.py migrate
