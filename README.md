# MLflow App: Dogs and Cat classification

# About project
This project uses MLflow to train and deploy a machine learning model that can classify images of dogs and cats. The model is built using a convolutional neural network (CNN) and is trained on a dataset of dog and cat images. The trained model is then deployed using MLflow and can be used to make predictions on new images.


# Description of components

# Steps
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


Step 1 - Create a repository by using template repository

Step 2 - Create a conda environment
```bash
conda create --prefix ./env python=3.7 -y
```

Step 3 - Activate the conda environment
```bash
conda activate ./env
```
<p align="center">or</p>

```bash
source activate ./env
```

Step 4 - Make requireed files and directories
```bash
python template.py
```

Step 5 - Make setup.py then install it
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