# Tarentula
Kind of spider

## Prerequisites

### Debian

```
apt-get update -y
apt-get install python-dev python-pip -y
pip install Jinja2
pip install Flask

pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0-cp27-none-linux_x86_64.whl
or
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.4.0-cp27-none-linux_x86_64.whl


```


### Server

```
FLASK_APP=server.py flask run --host 0.0.0.0
```

### Silk

```
python silk.py
```

### Terraria


Learning with few data in tarentual input.txt (beware of "by heart" learning)

```bash
python train.py --data_dir ../tarentula/ --batch_size 10 --seq_length 10 --num_epochs 100 --learning_rate 0.02
python sample.py -n 50
```
```
