conda create --prefix ./env python=3.7 -y
source activate ./env
pip install -r requirements.txt
conda install -c conda-forge tensorflow -y