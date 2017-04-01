# Swecha Machine Learning Workshop

## Setup

```bash
scripts/install_ext.sh # external dependencies
# setup virtual env
virtualenv --python=python3 basic
source basic/bin/activate
# now we have entered the virtual env
#  you prompt should looke like
#   (basic) username@compname:~/wherever/
pip install -r requirements.txt
# install virtualenv (basic) kernel to jupyter notebook
python3 -m ipykernel install --user --name=basic
# install pytorch
wget -c 'http://download.pytorch.org/whl/cu75/torch-0.1.11.post5-cp35-cp35m-linux_x86_64.whl'
pip install torch-0.1.11.post5-cp35-cp35m-linux_x86_64.whl
```
