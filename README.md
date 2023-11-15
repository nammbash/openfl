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

## How it Works

### Architecture
![Federated Learning](https://raw.githubusercontent.com/intel/openfl/develop/docs/images/diagram_fl_new.png)

## Requirements
- Ubuntu Linux 18.04+
- Python 3.7+ (recommended to use with [Virtualenv](https://virtualenv.pypa.io/en/latest/)).

OpenFL supports training with TensorFlow 2+ or PyTorch 1.3+ which should be installed separately. User can extend the list of supported Deep Learning frameworks if needed.

## Installation

You can simply install OpenFL from PyPI:

```
$ pip install openfl
```
For more installation options check out the [online documentation](https://openfl.readthedocs.io/en/latest/install.html).

## Getting Started


| workflow Mode | API | Flexibility | Ease of Use | SingleNode |  MultiNode | Real Federation Usage | 1.x support | 2.x support |
| -------------- | ----- | :--------------------: | :-----------------------: | :----------------------------: | :----------: | :----------: | :----------: | :----------: |
| Native | Python Native API | ❌ | ✅ | ✅ | ❌ | ❌ |  ✅ | ❌ |
| [Aggregator-based](https://openfl.readthedocs.io/en/latest/running_the_federation.html#aggregator-based-workflow) | Task Runner API | ✅ | ❌ | ✅ | ✅ | ✅ |  ✅ | ❌ |
| [Director-based](https://openfl.readthedocs.io/en/latest/running_the_federation.html#director-based-workflow) | Interactive API | ❌ | ✅ | ✅ | ✅ | ❌ |  ✅ | ✅ |
| [Experimental](https://openfl.readthedocs.io/en/latest/workflow_interface.html) | Workflow Interface API | ✅ | ✅ | ✅ | ❌ | ❌ |  ✅ | ✅ |

OpenFL enables data scientists to set up a federated learning experiment following one of the workflows:

- [Director-based Workflow](https://openfl.readthedocs.io/en/latest/running_the_federation.html#director-based-workflow):
Setup long-lived components to run many experiments in series. Recommended for FL research when many changes to model, dataloader, or hyperparameters are expected

- [Aggregator-based Workflow](https://openfl.readthedocs.io/en/latest/running_the_federation.html#aggregator-based-workflow):
Define an experiment and distribute it manually. All participants can verify model code and [FL plan](https://openfl.readthedocs.io/en/latest/running_the_federation.html#federated-learning-plan-fl-plan-settings) prior to execution. The federation is terminated when the experiment is finished

- [Workflow Interface](https://openfl.readthedocs.io/en/latest/workflow_interface.html) ([*experimental*](https://openfl.readthedocs.io/en/latest/experimental_features.html)):
Create complex experiments that extend beyond traditional horizontal federated learning. See the [experimental tutorials](https://github.com/intel/openfl/blob/develop/openfl-tutorials/experimental/) to learn how to coordinate [aggregator validation after collaborator model training](https://github.com/intel/openfl/tree/develop/openfl-tutorials/experimental/Workflow_Interface_102_Aggregator_Validation.ipynb), [perform global differentially private federated learning](https://github.com/psfoley/openfl/tree/experimental-workflow-interface/openfl-tutorials/experimental/Global_DP), measure the amount of private information embedded in a model after collaborator training with [privacy meter](https://github.com/intel/openfl/blob/develop/openfl-tutorials/experimental/Privacy_Meter/readme.md), or [add a watermark to a federated model](https://github.com/intel/openfl/blob/develop/openfl-tutorials/experimental/Workflow_Interface_301_MNIST_Watermarking.ipynb).

The quickest way to test OpenFL is to follow our [tutorials](https://github.com/intel/openfl/tree/develop/openfl-tutorials). </br>
Read the [blog post](https://towardsdatascience.com/go-federated-with-openfl-8bc145a5ead1) explaining steps to train a model with OpenFL. </br>
Check out the [online documentation](https://openfl.readthedocs.io/en/latest/index.html) to launch your first federation.

## Support
Please join us for our bi-monthly community meetings starting December 1 & 2, 2022! <br>
Meet with some of the OpenFL team members behind OpenFL. <br>
We will be going over our roadmap, open for Q&A, and welcome idea sharing. <br>

Calendar and links to a Community calls are [here](https://wiki.lfaidata.foundation/pages/viewpage.action?pageId=70648254)

Subscribe to the OpenFL mail list openfl-announce@lists.lfaidata.foundation


See you there!

We also always welcome questions, issue reports, and suggestions via:

* [GitHub Issues](https://github.com/intel/openfl/issues)
* [Slack workspace](https://join.slack.com/t/openfl/shared_invite/zt-ovzbohvn-T5fApk05~YS_iZhjJ5yaTw)

## License
This project is licensed under [Apache License Version 2.0](LICENSE). By contributing to the project, you agree to the license and copyright terms therein and release your contribution under these terms.


## Citation

```
@article{openfl_citation,
	author={Foley, Patrick and Sheller, Micah J and Edwards, Brandon and Pati, Sarthak and Riviera, Walter and Sharma, Mansi and Moorthy, Prakash Narayana and Wang, Shi-han and Martin, Jason and Mirhaji, Parsa and Shah, Prashant and Bakas, Spyridon},
	title={OpenFL: the open federated learning library},
	journal={Physics in Medicine \& Biology},
	url={http://iopscience.iop.org/article/10.1088/1361-6560/ac97d9},
	year={2022},
	doi={10.1088/1361-6560/ac97d9},
	publisher={IOP Publishing}
}
```

