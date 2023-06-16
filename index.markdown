---
layout: home
title: Portfolio
permalink: /portfolio/
background: '/images/bd_vis.jpg'
youtubeId: fjA3YFZK3E8
---
# Lukas Mueller

## SNHU, CS-499 Computer Science Capstone - MLDash

### Machine Learning Dashboard using OpenAI Gym, Tensorflow, Keras, MongoDB, and JupyterDash.

### Overview:
MLDash is a Jupyter Dash application that runs a reinforcement learning algorithm and writes training data to a MongoDB database, which it then converts into interactive data visualizations. An Anaconda environment was created to run the app, which connects to a MongoDB server. 
The CS_499 repository contains 5 snapshots of the MLDash application that span the development process (documentation added throughout development).

[Origin][ml-origin] - The Cartpole program and the Dashboard program, before any integration or upgrades

[Enhancement 1][ml-enhancea] - Software Design and Enginering (Requirements Analysis, Software Integration, Interface Design)

[Enhancement 2][ml-enhanceb] - Algorithms and Data Structure (optimization of speed and memory consumption)

[Enhancement 3][ml-enhancec] - Databases (Expansion of database and data handling capabilities)

[MLDash][ml-enhanced] - The most recent iteration of the final artifact, which includes security upgrades

The initial code review can be viewed here or on [YouTube][code-review].
{% include youtubePlayer.html id=page.youtubeId %}


The MLDash project was written in the Spring of 2023. As an aspiring machine learning engineer, and software engineer by discipline, I recognize the value in making complicated tasks more accessible to the common user. Training machine learning algorithms requires tuning their (sometimes numerous) hyperparameters and hoping that the changes made boost model performance, while also keeping track of the changes that have been made. The main purpose of this project is to simplify this task for users, automate record keeping, and generate data visualizations that can assist users in the selection of more optimal hyperparameters. While the project currently hosts a single AI algorithm, OpenAI Gym's Cartpole-v1, I anticipate that additional models can be added as modules over time. The algorithm used to solve the cartpole problem is a deep-Q reinforcement learning algorithm that solves the problem of balancing a pole attached to a cart that moves on a frictionless rail. The model acquires data from the environment (observation space) and determines which sequence of actions results in better performance for each situation. The model trains itself by replaying experiences it acquires, prioritizing samples of its experience based on how different those experiences were from its predictions. The model begins training with a higher likelihood to explore, allowing it to gather new experiences by trying different action sequences; as training continues, the model relies less on exploration and more on the exploitation of the experiences it has gathered. 

The MLDash program is centered around the Dashboard.ipynb file. This file creates an instance of the MLMongo class (defined in crud.py) to initiate a connection to a local MongoDB service. It also creates an instance of the Cartpole class, which makes use of several other classes: 
* DQNsolver (for the learning model setup, and learning procedures) 
* PrioritizedBuffer (an upgraded sampling procedure that makes experience replay a non-arbitrary process)
* ScoreLogger (to record hyperparameters and performance metrics)

During training, hyperparameter values and performance metrics are written to the metrics.csv file. The metrics collection and summary collection are contained in the MongoDB TRAIN database. When the model successfully balances the pole (for a minimum average duration) the metrics.csv file that contains training data is read into a Python dictionary and written to the TRAIN/metrics database collection. Once the database has been populated with training data, users can view this data using the dashboard. The dashboard allows the data to be viewed in the form of an interactive data table and dynamic data visualizations. Users have the ability to filter data to examine summary data and individual training sessions, and the accompanying charts change along with the data table.


This project was created by integrating a simpler dashboard program and a basic cartpole learning model implementation.
Various upgrades were made, along the way, in areas related to software engineering, algorithms and data structures,
and databases:

Additional functions were added to the crud.py, score_logger.py to facilitate local storage of learning model training
data, and the ability to write this data to a database. The Dashboard.ipynb file was upgraded to provide a relevant 
and task-specific interface with enhanced interactivity, dataframe filtering, data session indexing, and data 
visualization capabilities.

The learning algorithm itself enjoyed a significant upgrade that improved its ability to learn from its experiences.
During exprience replay (code found in dqn_solver.py) the batch sampling method was upgraded from using a random
sampling procedure to use prioritized sampling (code found in the prioritized_buffer.py file), resulting in a more
effective implementation of the learning algorithm and contributing to significant reduction in total memory use. 

 Enjoy!


This site was built using [GitHub Pages](https://pages.github.com/)

[MLDash on Github]: [ml-dash]
[README on GitGub]: [read-me]

[read-me]: https://github.com/lumutek/lumutek.github.io/blob/main/README.md
[ml-dash]: https://github.com/lumutek/CS-499/

[ml-origin]: https://github.com/lumutek/lumutek.github.io/tree/main/MLDash/1-Origin
[ml-enhancea]: https://github.com/lumutek/lumutek.github.io/tree/main/MLDash/2-Enhancement_1_Software_Design_and_Engineering
[ml-enhanceb]: https://github.com/lumutek/lumutek.github.io/tree/main/MLDash/3-Enhancement_2_Algorithms_and_Data_Structure
[ml-enhancec]: https://github.com/lumutek/lumutek.github.io/tree/main/MLDash/4-Enhancement_3_Databases
[ml-enhanced]: https://github.com/lumutek/lumutek.github.io/tree/main/MLDash/5-MLDash

[code-review]: https://youtu.be/fjA3YFZK3E8

