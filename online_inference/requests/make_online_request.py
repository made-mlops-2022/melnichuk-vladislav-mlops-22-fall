import pandas as pd
import json
import logging
import os
import requests

def main_online_inference():
    if not os.path.isdir("logs"):
        os.mkdir("logs")

    FORMAT_LOG = "%(asctime)s: %(message)s"
    file_log = logging.FileHandler("logs/fetcher.log")
    console_out = logging.StreamHandler()

    logging.basicConfig(
        handlers=(file_log, console_out),
        format=FORMAT_LOG,
        level=logging.INFO,
        datefmt="|%H|%M|%S|",
    )
    logger = logging.getLogger("Requests")

    data = pd.read_csv('./data/heart_cleveland_upload.csv').drop('condition', axis=1)
    data_requests = data.to_dict(orient='records')

    for request in data_requests:
        response = requests.post(
            'http://127.0.0.1:12000/predict',
            json.dumps(request)
        )
        logger.info('Online response:')
        logger.info(f'Status code: {response.status_code}')
        logger.info(f'Msg: {response.json()}')

# run 
main_online_inference()