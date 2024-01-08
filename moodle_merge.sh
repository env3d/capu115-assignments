#!/bin/bash

# Grades file to merge with
#GRADES_FILE="Grades-COMP 330 1AB - Fall 2023-Lab 4 Ingesting the BC Liquor dataset-2420901.csv"
GRADES_FILE=$1

oldIFS="$IFS"
IFS=$'\n':

# Merge the score into the grade files moodle expects
# User should redirect this to an output file
cat $GRADES_FILE | while read LINE
do
    ID=$(echo $LINE | cut -f 1 -d ,)
    SCORE=$(grep $ID _grades.csv | cut -f 3 -d ,)
    if [[ ! -z $SCORE ]]
    then
	    #echo $LINE | perl -pe "s/(.*?),.*/\1/"
	    echo $LINE | perl -pe "s/(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*)/\1,\2,\3,\4,\5,$SCORE,\7/"
    else
	    echo $LINE
    fi
done

IFS="$oldIFS"
