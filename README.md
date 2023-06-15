---
layout: page
title: MLDash Requirements
permalink: /readme/
---

## Created by Lukas Mueller

### SNHU, CS-499 Computer Science Capstone 

### Machine Learning Dashboard using OpenAI Gym, Tensorflow, MongoDB, and JupyterDash. 


#### Overviev: 
MLDash is currently a Jupyter Notebook application that reads to and writes from an MongoDB database. 
An Anaconda environment was created to run the notebook in. The CS_499 repository contains 5 snapshots of the MLDash
application that span the development process(documentation added throughout development):

1. Origin (The Catpole program and the Dashboard program, before any integration or upgrades)
 
2. Enhancement 1: Software Design and Enginering (Requirements Analysis, Software Integration, Interface Design)
 
3. Enhancement 2: Algorithms and Data Structures (optimization of speed and memory consumption)
 
4. Enhancement 3: Databases (Expansion of database and data handling capabilities)
 
5. MLDash (The most recent iteration of the final artifact, which includes security upgrades)



#### System requirements:

16 GB of physical RAM, assuming that normal system function takes around 4GB or less
Some virtual memory (Set to 8 GB, just in case)
CPU with speed of at least 1Ghz 
(There are no GPU requirements for this version, but CUDA enabled cores should be used automatcally if present on the host system)


#### Current Anaconda environment specifications:

Python 3.7.16 (will upgrade if possible)
gym=0.25.2
tensorflow==2.11.0
numpy==1.21.6
pandas==1.3.5
matplotlib==3.5.3
pygame==2.4.0
pyglet==2.0.7
jupyter-dash==0.4.2
dash==2.10.0
pymongo==4.3.3
dash_leaflet==0.1.23
notebook==6.5.2
ipykernal=6.16.2
statsmodels
dash-bootstrap-components

The Anaconda environment can be created by entering the following commands:

conda create --name MLDash python=3.7.16

conda activate MLDash

py -m pip install --upgrade pip

pip install gym=0.25.2 tensorflow==2.11.0 numpy==1.21.6 pandas==1.3.5 matplotlib==3.5.3 pygame==2.4.0 pyglet==2.0.7 jupyter-dash==0.4.2 dash==2.10.0 pymongo==4.3.3 dash_leaflet==0.1.23 notebook==6.5.2 ipykernal=6.16.2, statsmodels, dash-bootstrap-components


#### Install MongoDB as a local server instance. 

Install either MongoDB Compass (GUI) or the Mongo Shell (CLI) (mongosh was used by the developer, on Windows 10)

post-mongosh installation setup:

In the terminal, type the following commands:
(this allows you to set up the necessary databases, users, roles, and security mechnisms)
* mongosh
* show dbs
* use admin

* db.createUser({
  user: "admin",
  pwd: "youradminpassword",
  roles: [ { role: "dbAdminAnyDatabase", db: "admin" } ]
})

* db.auth('admin','youradminpassword')

* db.updateUser(
  'admin',
  {
    pwd: 'youradminpassword',
    mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ] 
 }
)

* use TRAIN
* db.createCollection("metrics")
* db.createCollection("summary")

* db.runCommand({ 
  createUser: "yourusername",
  pwd: "yourpassword",
  roles: [{ role: "readWrite", db: "TRAIN" }]
});

* db.updateUser(
  'yourusername',
  {
    pwd: 'yourpassword',
    mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ] 
 }
)

You can now exit Mongo Shell

Once this setup has been completed, the correct connection string is as follows
(This can be used to connect to the database using another program like MongoDB Compass):

mongodb://yourusername:yourpassword@localhost:27017/TRAIN?authMechanism=SCRAM-SHA-256


# Jupyter Notebook Setup

In order to apply the environment in Jupyter Notebook, type in the following command:

python -m ipykernel install --user --name=MLDash


Open Jupyter Notebook with the following command:

jupyter notebook


Open the Dashboard.ipynb in the project folder, wherever it was downloaded to on your machine


Use the "Kernel" tab at the top of the notebook to select the MLDash kernel


Run the notebook

(The user is presented with a login screen, which must be successfully authenticated to before any other MLDash content can be displayed. Simply use the credentials you created for the regular user during database setup. Once authenticated, the dashboard application will run inline with the Jupyter Notebook content, with an optional link that allows a user to view the dashboard fullscreen in their default browser.)
