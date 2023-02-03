conda create --prefix ./env python=3.7 -y
source activate ./env
python setup.py install
conda env export > conda.yaml
