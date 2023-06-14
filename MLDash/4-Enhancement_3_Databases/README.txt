MLDash is currently a Jupyter Notebook application. An Anaconda environment was created to run the notebook from. 

System requirements:
16 GB of physical RAM, assuming that normal system function takes around 4GB or less
Some virtual memory (4-8 GB, just in case)
CPU with speed of at least 1Ghz 
(There are no GPU requirements for this version)

Install MongoDB as a local server instance. 
Either install MongoDB Compass (GUI) or the Mongo Shell (CLI) (mongosh was used by the developer, on Windows 10)
post-mongosh installation setup:

1)In the terminal, type the following commands:
(this allows you to set up the necessary databases, users, roles, and security mechnisms)
mongosh
show dbs
use admin
use admin
db.createUser({
  user: "admin",
  pwd: "password",
  roles: [ { role: "dbAdminAnyDatabase", db: "admin" } ]
})

db.auth('admin','password')

db.updateUser(
  'admin',
  {
    pwd: 'password',
    mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ] 
 }
)

use TRAIN
db.createCollection("metrics")
db.createCollection("summary")
db.runCommand({ 
  createUser: "aiuser",
  pwd: "password",
  roles: [{ role: "readWrite", db: "TRAIN" }]
});
db.updateUser(
  'aiuser',
  {
    pwd: 'password',
    mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ] 
 }
)

Once this setup has been completed, the correct connection string is as follows
(This can be used to connect to the database using another program like MongoDB Compass):

mongodb://aiuser:password@localhost:27017/TRAIN?authMechanism=SCRAM-SHA-256


Current Anaconda environment specifications:
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


The Anaconda environment can be created by entering the following commands:

conda create --name MLDash python=3.7.16

conda activate MLDash

py -m pip install --upgrade pip

pip install gym=0.25.2 tensorflow==2.11.0 numpy==1.21.6 pandas==1.3.5 matplotlib==3.5.3 pygame==2.4.0 pyglet==2.0.7 jupyter-dash==0.4.2 dash==2.10.0 pymongo==4.3.3 dash_leaflet==0.1.23 notebook==6.5.2 ipykernal=6.16.2, statsmodels



In order to apply the environment in Jupyter Notebook, type in the following command:

python -m ipykernel install --user --name=MLDash


Open Jupyter Notebook with the following command:

jupyter notebook


Open the Dashboard.ipynb in the project folder, wherever it was downloaded to on your machine


Use the "Kernel" tab at the top of the notebook to select the MLDash kernel


Run the notebook

The dashboard application will run inline with the Jupyter Notebook content, but a link appears that allow
a user to view the dashboard fullscreen in their browser.