#!/bin/bash

# Scripts to initialize a test database, create necessary tables
# that Django does not have control over, then run tests

docker-compose up -d

docker cp $PWD/RubikVNdotOrg/db/rubikvn_schema.sql rbvn_mysql_database:/root

docker-compose exec db mysql -e "DROP DATABASE IF EXISTS test_rubikvn"
docker-compose exec db mysql -e "CREATE DATABASE test_rubikvn"

docker-compose exec db /bin/bash -c "mysql test_rubikvn < /root/rubikvn_schema.sql"

docker-compose exec web python manage.py test --keepdb
