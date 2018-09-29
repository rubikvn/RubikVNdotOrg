#!/bin/bash

# Install & set up virtualenv and project dependencies
first_time_install ()
{
  echo "Installing and setting up virtualenv..."
  sudo apt install python3.6-dev, libmysqlclient-dev, pv
  sudo python3.6 -m pip install virtualenv
}

initialize ()
{
  virtualenv rbvn-env/ -p python3.6
  source rbvn-env/bin/activate
  pip install -r requirements.txt
}

db_setup ()
{
  source rbvn-env/bin/activate

  echo -n "Your rubikvn01 user password for MySQL: "
  read -s MYSQL_PASSWORD
  echo

  # Create mysql database named wca
  echo "Importing the database export..."
  #echo "DROP DATABASE IF EXISTS wca; DROP DATABASE IF EXISTS rubikvn;" | mysql -u rubikvn01 --password=$MYSQL_PASSWORD
  #echo "CREATE DATABASE wca; CREATE DATABASE rubikvn;" | mysql -u rubikvn01 --password=$MYSQL_PASSWORD
  echo "CREATE DATABASE IF NOT EXISTS wca; CREATE DATABASE IF NOT EXISTS rubikvn;" | mysql -u rubikvn01 --password=$MYSQL_PASSWORD

  # Create the database schema
  echo "Making migrations for Django project"
  python3.6 manage.py makemigrations
  python3.6 manage.py migrate

  # Download & import WCA database
  echo "Downloading WCA database export..."
  cd RubikVNdotOrg/db/
  if [ -e WCA_export.sql ]
  then
    rm WCA_export.sql
  fi
  wget -q --show-progress https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip
  unzip WCA_export.sql.zip

  # Removing unnecessary files
  rm README.txt
  rm WCA_export.sql.zip

  pv WCA_export.sql | cat | mysql -u rubikvn01 --password=$MYSQL_PASSWORD wca

  # Extract from the database with our needed records
  echo "Reading from database wca and creating new database rubikvn..."
  pv vn_db_export.sql | cat | mysql -u rubikvn01 --password=$MYSQL_PASSWORD

  echo "Database updated on `date`" >> database_update.log

  cd ../../

  echo "-------------------------------"
  echo "Done setting up MySQL database."
}

dj_migrate ()
{
  source rbvn-env/bin/activate

  echo -n "Your rubikvn01 user password for MySQL: "
  read -s MYSQL_PASSWORD
  echo

  cd RubikVNdotOrg/db/
  pv vn_db_export.sql | cat | mysql -u rubikvn01 --password=$MYSQL_PASSWORD

  cd ../../

  python3.6 manage.py makemigrations
  python3.6 manage.py migrate
}

finish ()
{
  # Escape virtualenv
  deactivate
  echo "Finished installation. You can now run the server using 'python3.6 manage.py runserver'."
}

usage ()
{
  echo "USAGE: ./install.sh [-u]"
  echo "    ./install.sh        For first time installation"
  echo "    ./install.sh -u     From second time installation, tell the script to update the database only"
  echo "    ./install.sh -m     Make migrations whenever the database structure is changed, without downloading and running the WCA database export script."
}

# main script
# Parsing arguments using getopts
if [ $# -eq 0 ]
then
  first_time_install
  initialize
  db_setup
  finish
else
  while getopts ":um" opt; do
    case ${opt} in
      u )
        db_setup
        ;;
      m )
        dj_migrate
        ;;
      \?)
        usage
        ;;
    esac
  done
fi
