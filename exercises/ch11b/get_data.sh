#!/bin/bash
# Download all actor names and extract only 1950's onwards

FILE=name.basics.tsv

wget https://datasets.imdbws.com/${FILE}.gz
mv $FILE.gz _$FILE.gz
gunzip _${FILE}.gz
grep -E '\t195\d\t(\d{4}|\\N)\t.*' _${FILE} > ${FILE}
grep -E '\t20\d\d\t(\d{4}|\\N)\t.*' _${FILE} >> ${FILE}
rm _$FILE
sed -i '' 's/ /_/g' name.basics.tsv 
