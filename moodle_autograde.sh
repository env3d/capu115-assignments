#!/bin/bash

# This script represents a much easier way to perform autograding on moodle

if [[ $# -ne 2 ]]
then
    echo "Usage $0 <moodle assignment zip> <Unit test location>"
    exit 1
fi

# Unzip into temporary directory
unzip -d _students $1 >/dev/null

# The exercise folder containing the test.py file
#UNITTEST="./labs/lab1/test.py"
UNITTEST="$2"

# copy from template the test file to each user's directory
ls -d _students/* | awk -F, -v UNITTEST="$UNITTEST" '{print "cp " UNITTEST " \"" $1 "\""}' | bash

DIRS=$(ls -d _students/*)

oldIFS="$IFS"
IFS=$'\n':

echo -n "" > _grades.csv

# go into each directory and run test
for DIR in $DIRS
do
    cd $DIR
    OUTPUT=$(python3 test.py 2>&1 | head -n 1)
    TOTAL=$(echo -n $OUTPUT | wc -m | awk '{print $1}')
    SUCCESS=$(echo -n $OUTPUT | tr -d F | tr -d E | wc -m | awk '{print $1}') 
    FAILURES=$(echo -n $OUTPUT | tr -d . | wc -m | awk '{print $1}')
    # echo "TOTAL: $TOTAL, SUCCESS: $SUCCESS, FAILURES: $FAILURES"
    SCORE=$(echo "scale=2; $SUCCESS / $TOTAL * 100" | bc)
    SCORE_OUTPUT=$(echo "$DIR/$SCORE" | awk -F[_/] '{print "\"Participant "$4"\","$3","$7}')
    cd - > /dev/null
    
    # Record the score
    echo $SCORE_OUTPUT >> _grades.csv
done


IFS="$oldIFS"
cat _grades.csv

# clean up
rm -fr _students _grades.csv
