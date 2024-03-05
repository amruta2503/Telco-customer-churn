from source.constant import constant
from datetime import datetime
import os


class TrainingPipelineConfig:
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime('%m_%d_%Y_%H_%M_%S')

        self.target_column = constant.TARGET_COLUMN
        self.train_pipeline_name = constant.TRAIN_PIPELINE_NAME
        self.artifact_dir = os.path.join(constant.ARTIFACT_DIR,timestamp)
        self.mongodb_url_key = constant.MONGODB_URL_KEY
        self.database_name = constant.DATABASE_NAME
        self.collection_name = constant.DI_COLLECTION_NAME
        self.train_test_split_ratio = constant.DI_TRAIN_TEST_SPLIT_RATIO
        self.di_dir = os.path.join(self.artifact_dir,constant.DI_DIR_NAME)
        self.feature_store_file_path = os.path.join(self.di_dir,constant.DI_FEATURE_STORE_DIR,constant.FILE_NAME)
        self.train_filename = os.path.join(self.di_dir,constant.DI_INGESTED,constant.TRAIN_FILE_NAME)
        self.test_filename = os.path.join(self.di_dir,constant.DI_INGESTED,constant.TEST_FILE_NAME)







