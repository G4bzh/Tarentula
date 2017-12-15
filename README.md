# Tarentula
Web spider using Scrapy

## Prerequisites

### Debian

```
apt-get update -y
apt-get install python-dev python-lxml python-service-identity python-pip -y
pip install scrapy
pip install Twisted==16.4.1
pip install Jinja2
pip install nltk

pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0-cp27-none-linux_x86_64.whl
or
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp27-none-linux_x86_64.whl


python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('wordnet')
```
