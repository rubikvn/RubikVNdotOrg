#!/bin/bash

echo Starting database container...

docker-compose up -d db

cd RubikVNdotOrg\\db
if [ ! -d wca_export ]
then
    mkdir wca_export
else
    echo "Empty wca_export folder"
    rm -rf wca_export
    mkdir wca_export
fi

echo Done

echo Downloading WCA database export...

cd wca_export
wget https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip
unzip WCA_export.sql.zip

echo Done

echo Moving SQL scripts to container...

docker cp ..\\vn_db_import.sql rbvn_mysql_database:/root
docker cp WCA_export.sql rbvn_mysql_database:/root

echo Done

echo Running import scripts inside container...
cd ..\\..\\..
docker-compose exec db bin/bash -c "mysql -e 'CREATE DATABASE IF NOT EXISTS wca';"
docker-compose exec db bin/bash -c "mysql -u root --default-character-set=utf8mb4 wca < /root/WCA_export.sql"
docker-compose exec db bin/bash -c "mysql -u root < /root/vn_db_import.sql"

echo Done

docker-compose up -d web
docker-compose exec web python manage.py migrate
echo Done
