import json
import datetime
import logging
import logging.config
import logging.handlers

def get_logger(file_name) -> logging:
    #custom log
    logging.addLevelName(15, "DATA")
    logging.DATA = 15

    logger = logging.getLogger()
    logger.setLevel(logging.DATA)      

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s')       

    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(formatter)
    logger.addHandler(stream_hander)       

    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d")

    file_handler = logging.FileHandler(f'./log/{current_datetime}{file_name}.log', encoding="UTF-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

logger = get_logger('channel_info')



    
