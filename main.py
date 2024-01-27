# from textSummarizer.logging import logger

# logger.info("Testing cusom logging for our project")

import sys
from textSummarizer.exception import CustomException
from textSummarizer.logging import logging

def divide(x:int, y:int) -> int:
    try:
        output = x / y
        return output
        logging.info("output run successfully")
        
    except Exception as e:
        raise CustomException(e,sys)
        logging.info("error in calculations")
    

divide(4, 0)
        

