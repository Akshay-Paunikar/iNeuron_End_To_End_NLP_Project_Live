import os
import sys
from pathlib import Path
import urllib.request as request
import zipfile
from src.textSummarizer.logging import logging
from src.textSummarizer.exception import CustomException
from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline


# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
# except Exception as e:
#     logging.info(f"Error Occured during stage {STAGE_NAME}")
#     raise CustomException(e,sys)

STAGE_NAME = "Data Validation Stage"

try:
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logging.info(f"Error Occured during stage {STAGE_NAME}")
    raise CustomException(e,sys)