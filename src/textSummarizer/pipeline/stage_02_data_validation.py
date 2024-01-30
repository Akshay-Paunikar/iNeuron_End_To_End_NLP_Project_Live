import os
import sys
from src.textSummarizer.constants import *
from src.textSummarizer.utils.common import read_yaml, create_directories
from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.components.data_validation import DataValidation
from src.textSummarizer.logging import logging
from src.textSummarizer.exception import CustomException

class DataValidationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()