import argparse
import os
import shutil
from tqdm import tqdm
import logging
from src.utils.common import read_yaml, create_directories
from src.utils.model import log_model_summary
import random
import tensorflow as tf

STAGE = "BASE_MODEL_CREATION"

os.makedirs("logs",exist_ok = True)

logging.basicConfig(
    filename=os.path.join("logs", 'running_logs.log'), 
    level=logging.INFO, 
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    )


def main(config_path):
    IMG_SIZE = [180,180]
    BATCH_SIZE = 32
    # read config files
    config = read_yaml(config_path)

    params = config["params"]

    logging.info("layers defined")

    DATA_DIR = "data/unzip/PetImages"


    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="training",
    seed=42,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
    )

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        DATA_DIR,
        validation_split=0.2,
        subset="validation",
        seed=42,
        image_size=IMG_SIZE,
        batch_size=BATCH_SIZE
    )

    LAYERS = [
    tf.keras.layers.Input(shape=tuple(params["img_shape"])),
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3,3), activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    tf.keras.layers.Conv2D(32, (3,3), activation="relu"),
    tf.keras.layers.MaxPool2D(pool_size=(2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(8, activation="relu"),
    tf.keras.layers.Dense(2, activation="softmax")
    ]

    classifier = tf.keras.Sequential(LAYERS)

    logging.info(classifier.summary())

    train_ds = train_ds.prefetch(buffer_size=32)
    val_ds = val_ds.prefetch(buffer_size=32)

    # logging.info(f"base model summary:\n{log_model_summary(classifier)}")

    classifier.compile(
    optimizer=tf.keras.optimizers.Adam(params["lr"]),
    loss=params["loss"],
    metrics=params["metrics"]
    )

    EPOCHS = 1
    history  = classifier.fit(train_ds, epochs=EPOCHS, validation_data = val_ds)

    logging.info(history.history)
    
    path_to_model_dir = os.path.join(
        config["data"]["local_dir"],
        config["data"]["model_dir"])
    create_directories([path_to_model_dir])
    path_to_model = os.path.join(
        path_to_model_dir, 
        config["data"]["init_model_file"])
    classifier.save(path_to_model)
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