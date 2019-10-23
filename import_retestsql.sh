#!/bin/bash

DB_HOST='192.168.225.10'
DB_USER='gauntlet'

if [ "$#" -ne 1 ]; then
    echo "Please supply the path to the SQL file as an argument"
    exit 1
fi

SQLFILE=$1
DATABASE=`grep 'Database: gauntlet_' $SQLFILE | awk '{print $5}'`

# Get the MySQL password
read -s -p "[?] Please enter MySQL password for '$DB_USER': " PASSWORD

# Create the original database
echo -e "\n[*] Executing MySQL command: 'CREATE DATABASE "$DATABASE"';"
mysql -u"$DB_USER" -h"$DB_HOST" -p"$PASSWORD" -e "CREATE DATABASE $DATABASE;"
echo -e "[*] $DATABASE created"

# Add original assessment data to database
echo -e "[*] Importing assessment data"
mysql -u"$DB_USER" -h"$DB_HOST" -p"$PASSWORD" "$DATABASE" < $SQLFILE
echo -e "[*] Assessment data imported"

# prompt to delete SQL file, and delete if y
echo -e "[-]"
read -p "[?] Would you like to delete $SQLFILE? (y/n) " DELETE

if [ $DELETE == 'y' ]; then
    rm $SQLFILE
    echo -e "[*] $SQLFILE has been deleted"
fi
