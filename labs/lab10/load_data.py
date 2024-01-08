import pandas
import sqlite3
import os

"""
After running this script, a file called imdb.db will be
created.  Execute the following commands:

sqlite> .header off
sqlite> .mode csv
sqlite> .separator '\t'
sqlite> .output 'title.ratings.tsv'
sqlite> select * from ratings where tconst in (select tconst from basics where startYear like '202%' and titleType='movie');

sqlite> .output 'title.basics.tsv'
sqlite> select * from basics where startYear like '202%' and titleType='movie';

$ sed -i '' 's/ /_/g' title.basics.tsv

"""
def main():
    if not(os.path.exists('imdb.db')):
        conn=sqlite3.connect('imdb.db') 
        process_tsv('_title.basics.tsv', conn)
        process_tsv('_title.ratings.tsv', conn)            
    else:
        print('imdb.db already exist')

def process_tsv(filename, conn):
    reader = pandas.read_csv(filename, sep='\t', chunksize=10000)
    #t = reader.get_chunk()
    #process_one_frame(t)
    for t in reader:
        process_one_frame(filename.split('.')[1], t, conn)

def process_one_frame(tablename, t: pandas.DataFrame, conn: sqlite3.Connection):
    df = t.replace(to_replace='\\N', value=None)
    conn=sqlite3.connect('imdb.db')
    df.to_sql(tablename, conn, if_exists='append')
    return df
    

if __name__ == '__main__':
    main()
