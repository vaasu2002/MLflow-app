import logging
import os
from from_root import from_root
LOG_FILE = 'running_logs.log'

logs_path = os.path.join(from_root(),"logs",LOG_FILE)

print(logs_path)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH, 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
)
logging.info("adashgdjbasjbdas")