from MAINTAINCE import utils
from MAINTAINCE.entity import config_entity
from MAINTAINCE.entity import artifact_entity
from MAINTAINCE.exception import PredictionException
from MAINTAINCE.logger import logging


class DataIngestion:
    def  __init__(self,data_ingestion_config:config_entity.DataIngestionConfig():
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise PredictionException(e, sys)