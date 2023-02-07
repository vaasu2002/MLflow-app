import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
from src.utils.model import log_model_summary
import random
import tensorflow as tf

STAGE = "MODEL_TRAINING"

os.makedirs("logs",exist_ok = True)

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path):
    # Reading config files
    config = read_yaml(config_path)

    params = config["params"]

    logging.info("Defining layer")

    DATA_DIR = os.path.join(
    config["data"]["unzip_data_dir"],
    config["data"]["parent_data_dir"])

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    DATA_DIR,
    validation_split=params["validation_split"],
    subset="training",
    seed=params["seed"],
    image_size=params["img_size"],
    batch_size=params["batch_size"]
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        DATA_DIR,
        validation_split=params["validation_split"],
        subset="validation",
        seed=params["seed"],
        image_size=params["img_size"],
        batch_size=params["batch_size"]
    )

    train_ds = train_ds.prefetch(buffer_size=32)
    val_ds = val_ds.prefetch(buffer_size=32)

    # Loading the base model

    path_to_model = os.path.join(
        config["data"]["local_dir"],
        config["data"]["model_dir"], 
        config["data"]["init_model_file"])
    

    logging.info(f"Loading the base model from {path_to_model}")


    model = tf.keras.models.load_model(path_to_model)

    model.compile(
    optimizer=tf.keras.optimizers.Adam(params["lr"]),
    loss=params["loss"],
    metrics=params["metrics"]
    )

    logging.info(f"Starting training!")

    history  = model.fit(train_ds, epochs=params["epochs"], validation_data = val_ds)

    logging.info(history.history)
    
    path_to_model_dir = os.path.join(
        config["data"]["local_dir"],
        config["data"]["model_dir"])
    create_directories([path_to_model_dir])
    path_to_model = os.path.join(
        path_to_model_dir, 
        config["data"]["init_model_file"])
    model.save(path_to_model)
    logging.info(f"model is saved at : {path_to_model}")

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise 