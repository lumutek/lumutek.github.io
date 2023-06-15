---
layout: home
title: Portfolio
permalink: /portfolio/
background: '/images/bd_vis.jpg'
youtubeId: fjA3YFZK3E8
---
##Lukas Mueller##

###SNHU###

###CS-499 Computer Science Capstone - MLDash###

###Machine Learning Dashboard using OpenAI Gym, Tensorflow, MongoDB, and JupyterDash.###

####Overview:#### 
MLDash is currently a Jupyter Notebook application that reads to and writes from an MongoDB database. 
An Anaconda environment was created to run the notebook in. The CS_499 repository contains 5 snapshots of the MLDash
application that span the development process(documentation added throughout development).

[Origin][ml-origin] - The Cartpole program and the Dashboard program, before any integration or upgrades

[Enhancement 1][ml-enhancea] - Software Design and Enginering (Requirements Analysis, Software Integration, Interface Design)

[Enhancement 2][ml-enhanceb] - Algorithms and Data Structure (optimization of speed and memory consumption)

[Enhancement 3][ml-enhancec] - Databases (Expansion of database and data handling capabilities)

[MLDash][ml-enhanced] - The most recent iteration of the final artifact, which includes security upgrades

The initial [code review][code-review] can be viewed here or on YouTube.
{% include youtubePlayer.html id=page.youtubeId %}


    The MLDash project was written in the Spring of '23. As an aspiring machine learning engineer, 
and software engineer by discipline, I recognize the value in making complicated tasks more accessible to the common
user. Training machine learning algorithms requires tuning their (sometimes numerous) hyperparameters and hoping
that the changes made boost model performance, while also keeping track of the changes that have been made.
The main purpose of this project is to simplify this task for users, automate record keeping, and generate data
visualizations that can assist users in the selection of more optimal hyperparameters. While the project currently
hosts only one AI algorithm, OpenAI Gym's Cartpole-v1, I anticipate that additional models can be added as modules
over time. The algorithm used to solve the cartpole problem is a deep-Q reinforcement learning algorithm that solves the problem of balancing
a pole attached to a cart that moves on a frictionless rail. The model acquires data from the environment
(observation space) and determines which sequence of actions results in better performance for each situation. 
The model trains itself by replaying experiences it acquires, prioritizing samples of its experience based on how 
different those experiences were from its predictions. The model begins training with a higher likelihood to explore,
allowing it to gather new experiences by trying numerous different action sequences; as training continues, the model
relies less on exploration and more on the exploitation of the experiences it has gathered. 

    The MLDash program is centered around the Dashboard.ipynb file. This file creates an instance of the MLMongo class 
(defined in crud.py) to initiate a connection to a local MongoDB service. It also creates an instance of the Cartpole 
class, which makes use of the DQNsolver(for the learning model setup, and learning procedures), PrioritizedBuffer
(an upgraded sampling procedure that makes experience replay a non-arbitrary process), and ScoreLogger(used to record 
hyperparameter profiles along with key performance metrics) classes. During training, hyperparameter values and performance 
metrics are written to the metrics.csv file. The metrics collection and summary collection are contained in the MongoDB 
TRAIN database. When the model successfully balances the pole (for a minimum average duration) the metrics.csv file that 
contains training data is read into a Python dictionary and written to the TRAIN/metrics database collection. Once the 
database has been populated with training data, users can view this data using the dashboard. The dashboard allows the 
data to be viewed in the form of an interactive data table and dynamic data visualizations. Users have the ability to 
filter data to examine summary data and individual training sessions, and the accompanying charts change along with the 
datatable.

####Capstone Objectives & Enhancements####
Course Outcome 1: You EmployED strategies for building collaborative environments that enable diverse audiences to support organizational decision-making in the field of computer science by completing the following enhancements:
*Integration and redesign of the Cartpole artifact and Dashboard artifact produced an easy to use interface for users new to the topic of reinforcement learning.
*Refactoring of the code into a more modular form allows code to be more easily reused or repurposed, and easier to understand. 
*Detailed documentation in the form of inline code comments allow people to understand what the code is doing, even if they are not familiar with the technologies being used. 
*Addition of database write functionality allows past work to be a source of insight for any user.
*Code from various stages of development is stored on GitHub.
*The names of files, functions, and variables were updated to reflect the new context
 

###Course Outcome 2:### 
You DesignED, DevelopED, and DeliverED professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts by completing the following enhancements:
*Dashboard artifact data table an data charts were modified for use with data generated by the reinforcement learning algorithm, with additional data visualization graphics added, to provide intuitive representations that can assist users in task-specific problem solving.
*Enabled real-time animation during the training of the learning algorithm
*Created a detailed code review of the original artifacts, and additional documentation including updated code comments and a detailed README file.
*Removal of unreachable or unused code, and the refactoring of code to use an approach that is more object oriented. 

###Course Outcome 3:### 
You DesignED and EvaluateED computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices by completing the following enhancements:
*Implemented a major upgrade to the learning algorithm itself, changing the experience replay sampling method from random sampling to prioritized sampling, using a customized buffer. This reduced memory requirements by about 75%.
*Changed neural network optimizer to RMSprop, which uses 1/3 of the memory that the Adam optimizer did, due to the way it computes moving averages.
*Addition of data cleaning methods to the code responsible for rendering data charts with trendlines, so that the program ignores records that could cause division-by-zero conditions and records that do not contatain compatible data (the header, for example)

###Course Outcome 4:### You DemonstrateD an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals by completing the following enhancements:
*Integrated and repurposed the functionality of multiple programs, upgraded the new functionality, added new functionality, and refactored the code to be more modular.
*Designed a task-specific interface that addresses requirements of target users while making the task of training a reinforcemnt learning algorithm more user friendly.
*Dependencies were updated to reflect more recent versioning

###Course Outcome 5:### You DevelopED a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources by completing the following enhancements:
*Increased use of exception handling throughout the code
*Enabled the use of SCRAM-SHA-256 based authentication to the database, restricting access to users with valid credentials.
*Restricting visibility of Dashboard content until a user has been successfully authenticated.
*Addition of a security class to create a session-specific security object, resulting in secure encoding through the use of a single-use variable length, cryptographically secure random key. Instead of storing a fixed username and password in the source code as cleartext, user input to the login screen is acted upon by security object class methods. These methods generate a cryptographically secure random byte sequence using the secrets library, truncate it to the length of the byte translation of each credential, and XOR the credential with the modified random. The encoded credentials and security object are then used to create a database agent object that uses the security object to decode the credentials before inserting them into the connection string.


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

By using tool that helps cultivate data perspective and insights, the process of training a deep-Q reinforcement
learning algorithm becomes more intuitive for users, while reducing the cognitive burden associated with analyzing
huge amounts of data. Enjoy!

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

