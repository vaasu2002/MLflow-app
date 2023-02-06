import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories, unzip_file
from src.utils.data_mgmt import validate_image
import random
import urllib.request as req

STAGE = "DATA_INGESTION"

os.makedirs("logs",exist_ok = True)
logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
    )

def main(config_path:str):

    # Reading configration files
    config = read_yaml(config_path)
    URL = config["data"]["source_url"]
    local_dir = config["data"]["local_dir"]
    create_directories([local_dir])

    data_file = config["data"]["data_file"]
    data_file_path = os.path.join(local_dir, data_file)

    
    if not os.path.isfile(data_file_path):

        logging.info("downloading started...")
        filename, headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename:{filename} created with info \n{headers}")

    else:

        logging.info(f"filename:{data_file} already present")

    # Unzip ops
    unzip_data_dir = config["data"]["unzip_data_dir"]

    if not os.path.exists(unzip_data_dir):
        create_directories([unzip_data_dir])
        unzip_file(source=data_file_path, dest=unzip_data_dir) # unziping the data

    else:

        logging.info(f"Data already extracted")

    # Validating data
    validate_image(config)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    try:

        logging.info("\n")
        logging.info(f"Starting the {STAGE} stage!")
        main(config_path=parsed_args.config)
        logging.info(f"{STAGE} stage completed!")

    except Exception as e:
        logging.exception(e)
        raise 