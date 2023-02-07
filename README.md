# MLflow App: Dogs and Cat classification

This project uses MLflow to train and deploy a machine learning model that can classify images of dogs and cats. The model is built using a convolutional neural network (CNN) and is trained on a dataset of dog and cat images. The trained model is then deployed using MLflow and can be used to make predictions on new images.


## Description of components

#### 1) Data Ingestion: 
`getdata.py` is the script which performs data ingestion. The script is designed to download a dataset from a given URL to the local machine if it's not already present and then unzip it. The script also performs a validation of the data to check if the data is properly extracted.

#### 2) Base Model Creation: 
`base_model.py` is the script which performs the base model creation. It uses the Tensorflow library to create a simple convolutional neural network (CNN) for image classification. The script defines the architecture of the model, compiles it and logs the model summary.

#### 3) Model Training: 
`model_training.py` is the script which trains the base model created in the previous step. The script uses the training data, loss function, optimizer, and other parameters defined in the configuration file to train the model. The script logs the progress of the training process and saves the final model after the training is completed.

## Prerequisites
To run this project, you need the following packages:

- Numpy
- Tensorflow
- Keras
- MlFlow
- Matplotlib

## Steps
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.



Step 1 - Create a conda environment
```bash
conda create --prefix ./env python=3.7 -y
```

Step 2 - Activate the conda environment
```bash
conda activate ./env
```
<p align="center">or</p>

```bash
source activate ./env
```

Step 3 - Make requireed files and directories
```bash
python template.py
```

Step 4 - Make setup.py then install it
```bash
python setup.py install
```

Create conda.yaml file (for ML Flow)
```bash
conda env export > conda.yaml
```


Running init_setup.sh
```bash
bash init_setup.sh
```


Creating conda environment using conda.yaml
```bash
conda env create -f conda.yaml
```
Activate using whatver is the name


# Contributing
Contributions are welcome! Please open an issue or submit a pull request.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
