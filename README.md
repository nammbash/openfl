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
The Quick Start Guide showcases setting up a federation using the TaskRunner API on a single machine
|   |  | 
| -------------- | -------- |
| Containing 3 Participants | 1. Aggregator  <br/> 2. Collaborator1  <br/> 3. Collaborator2  |
| Guide can be extended easily to | > Participants on separate machines. <br/> > Any number of Collaborators. |

**Guide in few simple steps.** _(Tip: use fx --help for any command usage details)_
```
0. Setup Prerequisites: miniconda environment, any Proxies (if needed), FQDN etc.
1. Setup Aggregator Workspace: Specify amongst others the model to train using the right FL Plan.
2. Setup "Collaborator 1" Workspace: Setup made easy by using the aggregator workspace above.
3. Setup "Collaborator 2" Workspace: Setup made easy by using the aggregator workspace above.
4. Start the Aggregator.
5. Start the 2 Collaborators.
```
### Step 0: Prerequisites
#### _Setup FQDN_
```bash
export FQDN=<FQDN> # Enter your FQDN here
export no_proxy= localhost, <local machine IP>, <FQDN>
```
#### _Setup Miniconda environment_
```bash
conda create -n fedai python=3.10
conda activate fedai
```
#### _Install OpenFL from source_
```bash
git clone https://github.com/intel/openfl.git
python -m pip install -U pip setuptools wheel
cd openfl/
python -m pip install .
```
### _Step 1: Setup Aggregator (in the current terminal)_
#### _Step 1a: Set Aggregator variables._
```bash
export WORKSPACE_TEMPLATE=keras_cnn_mnist # Specify the model to train and associted "FL Plan".
```
#### _Step 1b: Set Aggregator Workspace Variables._
```bash
export WORKSPACE_NAME="my_federation"
export WORKSPACE_PATH_AGGR=${HOME}/${WORKSPACE_NAME}
```
#### _Step 1c: Setup Aggregator Workspace._
```bash
cd ${HOME}
fx workspace create --prefix ${WORKSPACE_PATH_AGGR} --template ${WORKSPACE_TEMPLATE}
cd ${WORKSPACE_PATH_AGGR}
pip install -r requirements.txt
fx plan initialize
```
#### _Step 1d: Certify Aggregator Workspace._
```bash
fx workspace certify
fx aggregator generate-cert-request --fqdn $FQDN
fx aggregator certify --fqdn $FQDN  # Press "y" when prompted.
```
#### _Step 1e: Zip/Export Aggregator Workspace._
```bash
fx workspace export # Zip/export Workspace to be able to be imported by collaborators for usage.
```
### Step 2: Setup Collaborator1 _(in new terminal of same machine)_. _(Tip:Press Ctrl+Alt+T)_
_Note: Steps for new terminal in another machines are similar expect for exchanging files(cp vs scp) between these machines_
#### _Step 2a: Setup Collaborator1 Variables._
```bash
export COLLAB_NUMBER=1 # need to define the collab number. (1 now, 2 later, etc)
```
```bash
conda activate fedai # If machine is different you need Step 0: Prerequisites.
export COLLAB_NAME=cob_${COLLAB_NUMBER}
export COLLAB_PATH=${HOME}/${COLLAB_NAME}
mkdir ${COLLAB_PATH}
```
#### _Step 2b: Setup Collaborator1 Workspace Variables._
```bash
export WORKSPACE_NAME="my_federation"
export WORKSPACE_PATH_AGGR=${HOME}/${WORKSPACE_NAME}
export WORKSPACE_PATH_COBR=${COLLAB_PATH}/${WORKSPACE_NAME}
```
#### _Step 2c: Setup Collaborator1 Workspace._
```bash
cp ${WORKSPACE_PATH_AGGR}/${WORKSPACE_NAME}.zip ${COLLAB_PATH}/${WORKSPACE_NAME}.zip
cd ${COLLAB_PATH}
fx workspace import --archive ${WORKSPACE_NAME}.zip # Import the copied workspace from aggregator
```
#### _Step 2d: Create Collaborator1 Workspace Certificate._
```bash
cd ${WORKSPACE_PATH_COBR}
fx collaborator create -n ${COLLAB_NAME} -d ${COLLAB_NUMBER}
fx collaborator generate-cert-request -n ${COLLAB_NAME}
```
#### _Step 2e: Certify collaborator workspace using a Certificate Authority (The Aggregator also serves as the CA here)_
```bash
cp ${WORKSPACE_PATH_COBR}/col_${COLLAB_NAME}_to_agg_cert_request.zip ${WORKSPACE_PATH_AGGR}/  # Send collaborator certificate to aggregator
```
**_Switch to Aggregator(CA) Terminal and certify the collaborator certificate and send it back to collaborator_.**
```bash
export COLLAB_NUMBER=1 #Specify the collaborator number whose certificate you want to certify
```
```bash
export COLLAB_NAME=cob_${COLLAB_NUMBER}
export COLLAB_PATH=${HOME}/${COLLAB_NAME}
export WORKSPACE_PATH_COBR=${COLLAB_PATH}/${WORKSPACE_NAME}
cd ${WORKSPACE_PATH_AGGR}
fx collaborator certify --request-pkg col_${COLLAB_NAME}_to_agg_cert_request.zip  # Certify the collaborator certificate. Press "y" when asked.
cp ${WORKSPACE_PATH_AGGR}/agg_to_col_${COLLAB_NAME}_signed_cert.zip ${WORKSPACE_PATH_COBR}/ # Send signed certificate back to collaborator
```
**_Return back to Collaborator Terminal and import the signed certificate sent from CA(Aggregator)._**
```bash
fx collaborator certify --import agg_to_col_${COLLAB_NAME}_signed_cert.zip #import signed certificate rfom CA.
```
### Step 3: Setup Collaborator2 _(in new terminal of same machine)_. _(Tip:Press Ctrl+Alt+T)_
#### _Step 3a same as Step 2a except for COLLAB_NUMBER below._
```bash
export COLLAB_NUMBER=2 # need to define the collab number. (1 now, 2 later, etc)
```
#### _Step 3b same as Step 2b_
#### _Step 3c same as Step 2c_
#### _Step 3d same as Step 2d_
#### _Step 3e same as Step 2e except for COLLAB_NUMBER below._
```bash
export COLLAB_NUMBER=2 # need to define the collab number. (1 now, 2 later, etc)
```
## Run the federation
_See [Modes and API](#modes-and-associated-api) for supported aggregation algorithms._
### Step 4: Start Aggregator (In Aggregator Terminal)
```bash
cd ${WORKSPACE_PATH_AGGR}
fx aggregator start
```
### Step 5: Start Collaborators (In Collaborator1 & Collaborator2 Terminals)
```bash
cd ${WORKSPACE_PATH_COBR}
fx collaborator start -n ${COLLAB_NAME}
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
