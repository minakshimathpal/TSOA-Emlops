# Pytorch Ligtning Model Experimentation Template

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white)![hydra](https://img.shields.io/badge/Config-Hydra_1.3-89b8cd)![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Main Technologies
PyTorch Lightning - a lightweight PyTorch wrapper for high-performance AI research. Think of it as a framework for organizing your PyTorch code.

Hydra - a framework for elegantly configuring complex applications. The key feature is the ability to dynamically create a hierarchical configuration by composition and override it through config files and the command line.

Pytorch Image Models - PyTorch Image Models (timm) is a collection of image models, layers, utilities, optimizers, schedulers, data-loaders / augmentations, and reference training / validation scripts that aim to pull together a wide variety of SOTA models with ability to reproduce ImageNet training results.

# Key Features

1. Supports [Pytorch Custom Models](https://pytorch.org/vision/stable/models.html), [Huggingface Models](https://huggingface.co/models) and [Timm Models](https://github.com/huggingface/pytorch-image-models).
2. Model Training and Evaluation using [Pytorch Lightning Framework](https://lightning.ai/).
3. [Docker Container Based Model Training and Evaluation](https://github.com/u6yuvi/dl-package/tree/main#using-docker-containers)
3. Experiments Configuration using [Hydra Template](https://hydra.cc/).
4. Experiment Logging using:
    1. [Tensorboard](https://www.tensorflow.org/tensorboard/get_started).
    2. [Mlflow](https://github.com/mlflow/mlflow/)
    3. [Aim](https://github.com/aimhubio/aim)
5. Data Versioning using Data Version Control


## 🚀  Quickstart

```bash
# clone project
git clone https://github.com/minakshimathpal/TSOA-Emlops-Deep-Learning-package
cd TSOA-Emlops-Deep-Learning-package

# [OPTIONAL] create conda environment
conda create -n myenv python=3.9
conda activate myenv

# install pytorch according to instructions
# https://pytorch.org/get-started/

# install requirements
pip install -r requirements.txt
```

Template contains example with cat vs Dog  classification.
When running ```python classifier/train.py``` or ```classifier_train``` you should see something like this:
<div align="center">

![](https://github.com/minakshimathpal/TSOA-Emlops-Deep-Learning-package/blob/main/artifacts/terminal.png)

</div>

## ⚡  Your Superpowers

<details>
<summary><b>Override any config parameter from command line</b></summary>

```bash
python classifier/train.py trainer.max_epochs=20 model.optimizer.lr=1e-4
```

> **Note**: You can also add new parameters with `+` sign.

```bash
python train.py +model.new_param="owo"
```

</details>

<details>
<summary><b>Train on CPU, GPU</b></summary>

```bash
# train on CPU
python classifier/train.py trainer=cpu

# train on 1 GPU
python classifier/train.py trainer=gpu

```
</details>

<details>
<summary><b>Train model with chosen experiment config</b></summary>

```bash
python classifier/train.py experiments=example
```
> **Note**: Experiment configs are placed in [configs/experiments/](configs/experiments/).
</details>

Running Experiments you would see somthing like this 
- Training using  ```classifier/train.py experiments=cat_dog```  or  ```classifier_train experiments=cat_dog``` :
<div align="center">

![](https://github.com/minakshimathpal/TSOA-Emlops-Deep-Learning-package/blob/main/artifacts/terminal.png)

</div>

- Evaluation using  ```classifier/eval.py experiments=cat_dog``` or ```classifier_eval experiments=cat_dog``` :
<div align="center">

![](https://github.com/minakshimathpal/TSOA-Emlops-Deep-Learning-package/blob/main/artifacts/terminal.png)

</div>

## DVC Configuration
#Set remote storage for storing data and model artifacts
```bash
dvc remote add -d local <path_to_local_directory>

#Push data to remote directory
dvc push data outputs

#Pull data from remote directory
dvc pull
```
## Maintainers
  1. Minakshi Mathpal
  2. Jyotish Chandrasenan
  3. Sridhar Baskaran
  4. Ebin
