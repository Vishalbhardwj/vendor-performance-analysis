import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# logging structure
logging.basicConfig(
    filename='../logs/ingestion_db.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',
    force=True
)

engine = create_engine('sqlite:///../data/database/inventory.db')


def ingest_db(df, table_name, engine):
    ''' this function will ingest the dataframe into database table '''
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)


def load_raw_data():
    ''' this function will load CSVs as dataframe and ingest into db '''
    start = time.time()

    for file in os.listdir('../data/raw_data'):
        if file.endswith('.csv'):

            print(f"Ingesting: {file}")
            logging.info(f"Ingesting {file} in db.")

            df = pd.read_csv('../data/raw_data/' + file)

            print(f"Rows: {len(df)}")

            ingest_db(df, file[:-4], engine)

            print(f"Completed: {file}")
            logging.info(f"Completed {file}")

    end = time.time()
    total_time = (end - start) / 60

    logging.info("----------------Ingestion Complete-------------------")
    logging.info(f"Total Time Taken In Ingestion {total_time}")

    print("--------------- Ingestion Complete ---------------")
    print(f"Total Time Taken: {total_time:.2f} minutes")


if __name__ == '__main__':
    load_raw_data()