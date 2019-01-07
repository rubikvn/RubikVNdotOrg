#!/bin/bash

ORIGINAL_DIR=$PWD

echo -e "\033[1;36mStarting database container...\033[0m"

docker-compose up -d db

cd $PWD/RubikVNdotOrg/db
if [ ! -d wca_export ]
then
    mkdir wca_export
else
    rm -f wca_export/*
fi

echo -e "\033[1;32mDone\033[0m"


cd wca_export
if [ "$1" = "--fake" ]
then
    echo -e "\033[1;36mRunning SQL scripts...\033[0m"
    docker cp ../rubikvn_init.sql rbvn_mysql_database:/root
    cd $ORIGINAL_DIR
    docker-compose exec db /bin/bash -c "mysql -u root rubikvn < /root/rubikvn_init.sql"
    echo -e "\033[1;32mDone\033[0m"
else
    echo -e "\033[1;36mDownloading WCA database export...\033[0m"
    wget https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip
    unzip WCA_export.sql.zip


    echo -e "\033[1;32mDone\033[0m"

    echo -ne "\033[1;36mMoving SQL scripts to container...\033[0m"

    docker cp ../vn_db_import.sql rbvn_mysql_database:/root
    docker cp WCA_export.sql rbvn_mysql_database:/root

    echo -e "\033[1;32mDone\033[0m"

    echo -e "\033[1;36mRunning import scripts...\033[0m"
    cd $ORIGINAL_DIR
    docker-compose exec db /bin/bash -c "mysql -e 'CREATE DATABASE IF NOT EXISTS wca';"
    docker-compose exec db /bin/bash -c "mysql -u root --default-character-set=utf8mb4 wca < /root/WCA_export.sql"
    docker-compose exec db /bin/bash -c "mysql -u root < /root/vn_db_import.sql"

    echo -e "\033[1;32mDone\033[0m"
fi

docker-compose up -d web
docker-compose exec web python manage.py migrate
echo -e "\033[1;32mDone\033[0m"
