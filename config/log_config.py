import logging

def log_config():
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(module)s.%(funcName)s (line %(lineno)d): %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
