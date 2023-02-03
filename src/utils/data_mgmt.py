import shutil
import imghdr
import os
from PIL import Image
import logging
from src.utils.common import create_directories

def validate_image(config: dict) -> None:
    PARENT_DIR = os.path.join(
        config["data"]["unzip_data_dir"],
        config["data"]["parent_data_dir"])
    BAD_DATA_DIR = os.path.join(
        config["data"]["unzip_data_dir"],
        config["data"]["bad_data_dir"])
    create_directories([BAD_DATA_DIR])
    print(PARENT_DIR)
    print(BAD_DATA_DIR)
    for dirs in os.listdir(PARENT_DIR):
        print(dirs)
        full_path_data_dir = os.path.join(PARENT_DIR, dirs)
        print(full_path_data_dir)
        # print(os.listdir(full_path_data_dir))
        for imgs in os.listdir(full_path_data_dir):
            if(imgs!='Thumbs.db'):
                path_to_img = os.path.join(full_path_data_dir, imgs)
                try:
                    img = Image.open(path_to_img)
                    # print(img)
                    img.verify()

                    # print(imghdr.what(path_to_img))
                    # print(len(img.getbands()))
                    if len(img.getbands()) !=3 or imghdr.what(path_to_img) not in ['jpeg','png','jpg']:
                        bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                        shutil.move(path_to_img, bad_data_path)
                        logging.info(f"{path_to_img} not of expected format")
                        continue
                        
                except Exception as e:
                    print(f"{path_to_img} not of expected format")
                    bad_data_path = os.path.join(BAD_DATA_DIR, imgs)
                    shutil.move(path_to_img, bad_data_path)
                    print(f"moved bad file from {path_to_img} to {bad_data_path}")
                    print(e)

    print("Ok executed!")