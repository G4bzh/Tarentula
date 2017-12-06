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

python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('averaged_perceptron_tagger')
>>> nltk.download('wordnet')
```
