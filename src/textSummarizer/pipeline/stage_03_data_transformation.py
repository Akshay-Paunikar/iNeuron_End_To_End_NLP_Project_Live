import os
import sys
from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_transformation import DataTransformation
from src.textSummarizer.logging import logging
from src.textSummarizer.exception import CustomException

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()