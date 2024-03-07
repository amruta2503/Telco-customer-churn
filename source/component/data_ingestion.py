import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from source.exception import ChurnException
import os
from pymongo.mongo_client import MongoClient


class DataIngestion:

    def __init__(self,utility_config):
        self.utility_config = utility_config

    def export_data_into_feature_store(self):
        try:
            logging.info("start:data load from mongoDB")

            client = MongoClient(self.utility_config.mongodb_url_key)
            database = client[self.utility_config.database_name]
            collection = database[self.utility_config.collection_name]

            cursor = collection.find()

            data = pd.DataFrame(list(cursor))

            dir_path = os.path.dirname(self.utility_config.feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            data.to_csv(self.utility_config.feature_store_file_path,index=False)

            logging.info("complete:data load from mongoDB")

            return data
        except ChurnException as e:
            raise e

    def split_data_train_test(self,data):
        try:
            logging.info("Start:data train test split")

            train_set,test_set = train_test_split(data,train_size=self.utility_config.train_test_split_ratio,random_state=45)

            dir_name = os.path.dirname(self.utility_config.train_filename)
            os.makedirs(dir_name,exist_ok=True)

            train_set.to_csv(self.utility_config.train_filename,index=True)

            test_set.to_csv(self.utility_config.test_filename,index=True)

            logging.info("Complete:data train test split")
        except ChurnException as e:
            pass

    def clean_data(self,data):
        try:
            pass
        except ChurnException as e:
            pass

    def process_data(self,data):
        try:
            pass
        except ChurnException as e:
            pass

    def initiate_data_ingestion(self):
        data=self.export_data_into_feature_store()
        self.split_data_train_test(data)