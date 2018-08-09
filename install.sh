#!/bin/bash

# Install & set up virtualenv and project dependencies
echo "Installing and setting up virtualenv..."
sudo python3 -m pip install virtualenv
virtualenv rbvn-env/ -p python3
source rbvn-env/bin/activate
python3 -m pip install -r requirements.txt

echo -n "Your root user password for MySQL: "
read -s MYSQL_PASSWORD
echo

# Create mysql database named wca
echo "Importing the database export..."
echo "CREATE DATABASE IF NOT EXISTS wca; CREATE DATABASE IF NOT EXISTS rubikvn;" | mysql -u root --password=$MYSQL_PASSWORD

# Create the database schema
echo "Making migrations for Django project"
python3 manage.py makemigrations
python3 manage.py migrate

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

mysql -u root --password=$MYSQL_PASSWORD wca < WCA_export.sql

# Extract from the database with our needed records
echo "Reading from database wca and creating new database rubikvn..."
mysql -u root --password=$MYSQL_PASSWORD < vn_db_export.sql

echo "-------------------------------"
echo "Done setting up MySQL database, you can now run the server."

# Escape virtualenv
deactivate
