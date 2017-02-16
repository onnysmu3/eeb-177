#! /bin/bash

# this script will replace all carriage returns \r with new lines \n

cat $1 | tr "\r" "\n"  > formatted_$1

# the next line will replace all extra commas and will replace the contents of formatted_eBird_data.csv

sed 's/,\s/ /g' formatted_$1 > formatted_$1


