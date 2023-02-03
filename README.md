# Project Name

# About project

# Description of components

# Steps
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