# Swecha Machine Learning Workshop

Yet another Machine Learning workshop for beginners. Usually I tend to cram a lot of stuff into the [slides](http://suriyadeepan.github.io/4ccon) and overwhelm myself and the participants. This time, I am gonna try to teach as little as possible. 

## Setup

```bash
git clone https://github.com/suriyadeepan/swecha-machine-learning-workshop
cd swecha-machine-learning-workshop/
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
```

## Run Notebook

```bash
cd notebooks/
jupyter notebook
# make sure the kernel point to `basic`
```
