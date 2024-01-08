#!/bin/bash
# Download all actor names and extract only 1950's onwards

FILES="title.basics.tsv title.ratings.tsv"

for FILE in $FILES
do
    wget https://datasets.imdbws.com/${FILE}.gz
    mv $FILE.gz _$FILE.gz
    gunzip _${FILE}.gz
    
    #grep -E '\t195\d\t(\d{4}|\\N)\t.*' _${FILE} > ${FILE}
    #grep -E '\t20\d\d\t(\d{4}|\\N)\t.*' _${FILE} >> ${FILE}
    #rm _$FILE
    #sed -i '' 's/ /_/g' name.basics.tsv
done

grep -E '.*\tmovie\t.*\t.*\t.*\t202[0-9]\t' _title.basics.tsv > title.basics.tsv
cut -f 1 title.basics.tsv | xargs -I{} grep {} _title.ratings.tsv >> title.ratings.tsv
