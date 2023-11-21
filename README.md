<div align="center">
  <img src="https://github.com/securefederatedai/artwork/blob/main/PNG/OpenFL%20Logo%20-%20color.png?raw=true">
</div>

[![PyPI - Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)](https://pypi.org/project/openfl/)
[![Ubuntu CI status](https://github.com/intel/openfl/actions/workflows/ubuntu.yml/badge.svg)](https://github.com/intel/openfl/actions/workflows/ubuntu.yml)
[![Windows CI status](https://github.com/intel/openfl/actions/workflows/windows.yml/badge.svg)](https://github.com/intel/openfl/actions/workflows/windows.yml)
[![Documentation Status](https://readthedocs.org/projects/openfl/badge/?version=latest)](https://openfl.readthedocs.io/en/latest/?badge=latest)
[![Downloads](https://pepy.tech/badge/openfl)](https://pepy.tech/project/openfl)
[![DockerHub](https://img.shields.io/docker/pulls/intel/openfl.svg)](https://hub.docker.com/r/intel/openfl)
[![PyPI version](https://img.shields.io/pypi/v/openfl)](https://pypi.org/project/openfl/)
[<img src="https://img.shields.io/badge/slack-@openfl-blue.svg?logo=slack">](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw) 
[![License](https://img.shields.io/badge/License-Apache%202.0-brightgreen.svg)](https://opensource.org/licenses/Apache-2.0)
[![Citation](https://img.shields.io/badge/cite-citation-brightgreen)](https://arxiv.org/abs/2105.06413)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6599/badge)](https://bestpractices.coreinfrastructure.org/projects/6599)
<a href="https://scan.coverity.com/projects/securefederatedai-openfl">
  <img alt="Coverity Scan Build Status"
       src="https://scan.coverity.com/projects/29040/badge.svg"/>
</a>
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/intel/openfl/blob/develop/openfl-tutorials/interactive_api/numpy_linear_regression/workspace/SingleNotebook.ipynb)

## Introduction
Open Federated Learning (OpenFL) is a Python 3 framework for Federated Learning. OpenFL is designed to be a _flexible_, _extensible_ and _easily learnable_ tool for data scientists. OpenFL is hosted by The Linux Foundation, aims to be community-driven, and welcomes contributions back to the project.

Landed Looking for the Open Flash Library project also referred to as OpenFL? Find it [here](https://github.com/openfl/openfl)!

| OpenFL | Readme Links | 
| -------------- | :--------------------: | 
| BackGround | [OpenFL Background](BACKGROUND.md) |
| Supported Aggregation Algorithms |[OpenFL Aggregation Algorithms](AGGREGATION-ALGOS.md) |

### What is Federated Learning
[Federated learning](https://en.wikipedia.org/wiki/Federated_learning) is a distributed machine learning approach that enables collaboration on machine learning projects without having to share sensitive data, such as, patient records, financial data, or classified information. The minimum data movement needed across the federation is solely the model parameters and their updates.

## Quick Start Guide
### Clone this Repository
```
export WORKSPACE=</workspace/path>

git clone [https://github.com/securefederatedai/openfl.git $WORKSPACE/intel-nlp-toolkit](https://github.com/securefederatedai/openfl.git)
cd $WORKSPACE/
```

### Create a New Python  (Conda or Venv) Environment With Env Name: "fedai"
```shell
conda create -n fedai python=3.10
conda activate fedai
```
or
```shell
python -m venv fedai
source fedai
```

### Install Packages For Running OpenFL in <Aggregator> Mode 
```shell
pip install -r requirements.txt
```

## Run the federation
See [Modes and API](#modes-and-associated-api) for supported aggregation algorithms.
```shell
<mode>   mode you want to trigger.

sh aggregator_based_mode.sh
or
sh Fedai.sh <mode>
```

## How it Works
### Architecture
![Federated Learning](https://raw.githubusercontent.com/intel/openfl/develop/docs/images/diagram_fl_new.png)

## Get Started with detailed guides
For more installation options check out the [online documentation](https://openfl.readthedocs.io/en/latest/install.html). <br>
OpenFL enables data scientists to set up a federated learning experiment following one of the workflows using the associated API, each with its own benefits <br>

| Notes | Links | 
| -------------- | ----- |
Quick Test OpenFL using     | [Quick Start steps for singlenode](#quick-start-guide) |
Quickest Start OpenFL using | [Tutorials](https://github.com/intel/openfl/tree/develop/openfl-tutorials) |
Read                        | [Blog Post](https://towardsdatascience.com/go-federated-with-openfl-8bc145a5ead1) explaining steps to train a model with OpenFL |
Launch Federation using     | [Online Documentation](https://openfl.readthedocs.io/en/latest/index.html) to launch your first federation |

### Modes and associated API
| API | Flexibility | Ease of Use | SingleNode |  MultiNode | Real Federation Usage | 1.x support | 2.x support |
| -------------- | :--------------------: | :-----------------------: | :----------------------------: | :----------: | :----------: | :----------: | :----------: |
| [ Task Runner](https://openfl.readthedocs.io/en/latest/running_the_federation.html#aggregator-based-workflow "Define an experiment and distribute it manually. All participants can verify model code and FL plan prior to execution. The federation is terminated when the experiment is finished") | ✅ | ❌ | ✅ | ✅ | ✅ |  ✅ | ❌ |
| Python Native | ❌ | ✅ | ✅ | ❌ | ❌ |  ✅ | ❌ |
| [Interative](https://openfl.readthedocs.io/en/latest/running_the_federation.html#director-based-workflow "Setup long-lived components to run many experiments in series. Recommended for FL research when many changes to model, dataloader, or hyperparameters are expected") | ❌ | ✅ | ✅ | ✅ | ❌ |  ✅ | ✅ |
| [Workflow Interface](https://openfl.readthedocs.io/en/latest/workflow_interface.html "Create complex experiments that extend beyond traditional horizontal federated learning. See the experimental tutorials to learn how to coordinate aggregator validation after collaborator model training, perform global differentially private federated learning, measure the amount of private information embedded in a model after collaborator training with privacy meter, or add a watermark to a federated model")  | ✅ | ✅ | ✅ | ❌ | ❌ |  ✅ | ✅ |

## Support
**Join us:** bi-monthly community meetings to meet with some team members behind OpenFL for discussions on our roadmap, open Q&A, & idea sharing. <br>
**Calendar and links to Community calls:** [here](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=70648254) <br>
**Subscribe to the OpenFL mail list:** openfl-announce@lists.lfaidata.foundation

We also always welcome questions, issue reports, and suggestions via:
* [GitHub Issues](https://github.com/intel/openfl/issues)
* [Slack workspace](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw)

## License
This project is licensed under [Apache License Version 2.0](LICENSE). By contributing to the project, you agree to the license and copyright terms therein and release your contribution under these terms.
