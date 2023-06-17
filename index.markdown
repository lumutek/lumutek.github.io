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
##### MLDash is a Jupyter Dash application that runs a reinforcement learning algorithm and writes training data to a MongoDB database, which it then converts into interactive data visualizations. An Anaconda environment was created to run the app, which connects to a MongoDB server. 

### Professional Self-Assessment
##### The CS-499 Computer Science capstone was a challenging, but rewarding, exercise of the skills I have developed throughout the pursuit of my BS in Computer Science. I chose to integrate two code artifacts and repurpose their functionality to showcase particular skills that will my serve me in my future career as a software engineer, machine learning engineer, or data scientist. Additionally, the chosen artifacts represent work done in software design and engineering, algorithms and data structures, and databases, which represent in-demand computer science skills. Enhancements to the artifacts were made according to a well-considered plan, and instructor feedback was continuously integrated along the way, resulting in a single artifact with functionality that is greater than the sum of its parts. These efforts gave rise to the MLDash application. For this project I chose to work with code that is Python-compatible, using Jupyter Dash for interface, MongoDB for data storage and retrieval, Tensorflow with Keras for the core algorithm and data generation, and a variety of Python-based solutions to facilitate software integration and additional functionality. One of the most useful things a software engineer can do for users is to make complicated tools simple to use and user friendly. Training artificial intelligence models is a task that is difficult to understand and which can consume a lot of time. Additionally, keeping track of the relative performance of different versions of a model can be tedious or even intractable. The impetus behind MLDash is the simplification of this process. Record keeping is automated, and viewing the backend code is optional. Data from successful training sessions can be viewed in a filter-enabled data table, accompanied by data visualization graphics that make understanding the relationship between hyperparameters and performance metrics more intuitive. Training sessions completed by others can be uploaded to the MongoDB database to facilitate collaboration in the task of discovering the optimal combination of hyperparameters to produce the best model performance. Code documentation saw significant contributions in the form of code comments and a README file that includes detailed information about system requirements, dependency versions, and installation instructions. The code for MLDash was made more modular and object oriented through the conversion of new and existing functions into classes; this contributed to a more elegant integration of the primitive artifacts and allows other people to understand the code more easily. Regular updates on my progress were provided to my instructor which delineated the progress made, problems encountered, and the near-term and long-term direction of the project. In the category of software development and engineering, I successfully integrated two distinct programs, added additional functionality, upgraded existing functionality, and designed the MLDash application based on the requirements of target users (novices to artificial intelligence that wanted entry-level exposure to the technology). In the category of algorithms and data structures, I overhauled the reinforcement learning algorithm's core method of learning from its own experiences. The MLDash artifact does not perform random sampling of its experiences to learn, but instead performs prioritized sampling which identifies experiences that did not conform to the model's predictions, and emphasizes these experiences, to form a better predictive model (another effect of this implementation was a significant reduction in the amount of memory needed to solve the reinforcement learning problem, reducing the required amount of combined physical RAM and virtual memory from 80-100GB to 16-32GB, a 2.5 to 6.25 reduction factor). Additional improvements in memory efficiency were gained through the use of an alternative neural network optimizer. While the RMSprop optimizer is slightly less accurate than the Adam optimizer, it only uses about a third of the memory due to different methods of computing moving averages (The slight loss in accuracy was more than compensated for by the upgraded sampling method, and limiting memory consumption is of paramount importance if the program is to be useful for the target audience, who may not have extraordinary computer hardware at their disposal). In the category of databases, the CRUD database functionality (create, read, update, and delete) was upgraded to include write capabilities. During reinforcement learning, hyperparameters and performance metrics are written to a CSV file; if the model is successful, the CSV file is read into a Python dictionary (equivalent to a C++ hash table) and written to the MongoDB database. Data written to the database appears in the interface as an interactive data table and interactive charts, allowing users to make observations about the relative performance of different model instances, as well as the performance of individual instances, as well. In the category of security, the database authentication string was upgraded to require the use of the SCRAM-SHA-256 authentication mechanism, and the code was modified so that the authentication credentials used in the connection string were note storered in the code itself. The interface was modified to prompt users for a valid username and password, which are specified by a MongoDB admin user; the main content of the program is not displayed until a user successfully authenticates. A security class was created, the instances of which utilized a cryptographically secure single-use byte sequence, derived from the secrets library. The secure byte-sequence is truncated to the length of both the username and password input byte-translations, and the credentials are XORed against the relevant variable length sequence, then converted to hexidecimal. The encoded credentials and security object are then used to create a CRUD-capable MongoDB agent object, which decodes the credentials and inserts them into the database connection string. The code then attempts to ping the database server, only giving access to the dashboard content when the ping operation is successful. 
	
##### While I have worked on many coding projects throughout my academic career, I found the MLDash project to be particularly rewarding. The Pythonic combination of artificial intelligence, database manipulation, data visualization, software engineering, and secure coding was one that will help me to prepare for even more challenging projects in my chosen career as a machine learning engineer. My skills in planning, research, communication, and time management also contributed to the overall success of my plan for the Computer Science Capstone. As I continue to develop my skills in computer science, I will use what I have learned to make significant contributions to the teams and organizations I work with, and I look forward to what the future will bring.

### Artifacts (The Dashboard and Cartpole artifacts are combined in the MLDash artifact in Enhancement 1)

##### The CS_499 Github repository contains 5 snapshots of the MLDash application that span the development process (documentation added throughout development). Here are links to all of the code:

##### [Origin][ml-origin] - The Cartpole program and the Dashboard program, before any integration or upgrades

##### [Enhancement 1][ml-enhancea] - Software Design and Enginering (Requirements Analysis, Software Integration, Interface Design)

##### [Enhancement 2][ml-enhanceb] - Algorithms and Data Structure (optimization of speed and memory consumption)

##### [Enhancement 3][ml-enhancec] - Databases (Expansion of database and data handling capabilities)

##### [MLDash][ml-enhanced] - The most recent iteration of the final artifact, which includes security upgrades


### Highlights
##### The MLDash program is centered around the Dashboard.ipynb file. This file creates an instance of the MLMongo class (defined in crud.py) to initiate a connection to a local MongoDB service. It also creates an instance of the Cartpole class, which makes use of several other classes: 
* DQNsolver (for the learning model setup, and learning procedures) 
* PrioritizedBuffer (an upgraded sampling procedure that makes experience replay a non-arbitrary process)
* ScoreLogger (to record hyperparameters and performance metrics)

##### During training, hyperparameter values and performance metrics are written to the metrics.csv file. The metrics collection and summary collection are contained in the MongoDB TRAIN database. When the model successfully balances the pole (for a minimum average duration) the metrics.csv file that contains training data is read into a Python dictionary and written to the TRAIN/metrics database collection. Once the database has been populated with training data, users can view this data using the dashboard. The dashboard allows the data to be viewed in the form of an interactive data table and dynamic data visualizations. Users have the ability to filter data to examine summary data and individual training sessions, and the accompanying charts change along with the data table.

##### This project was created by integrating a simpler dashboard program and a basic cartpole learning model implementation. Various upgrades were made, along the way, in areas related to software engineering, algorithms and data structures, and databases:

##### Additional functions were added to the crud.py, score_logger.py to facilitate local storage of learning model training data, and the ability to write this data to a database. The Dashboard.ipynb file was upgraded to provide a relevant and task-specific interface with enhanced interactivity, dataframe filtering, data session indexing, and data visualization capabilities.

##### The learning algorithm itself enjoyed a significant upgrade that improved its ability to learn from its experiences. During experience replay (code found in dqn_solver.py) the batch sampling method was upgraded from using a random sampling procedure to use prioritized sampling (code found in the prioritized_buffer.py file), resulting in a more effective implementation of the learning algorithm and contributing to significant reduction in total memory use. 

###### The initial code review (informal) can be viewed here or on [YouTube][code-review].
{% include youtubePlayer.html id=page.youtubeId %}

#### Check out my blog posts (narratives), below, to learn more about my coding journey... or jump to a particular narrative using these links:

[Initial enhancement plan][enhancement-plan]
[Enhancement #1 Narrative: Software Development and Engineering][enhance-one]
[Enhancement #2 Narrative: Algorithms and Data Structures][enhance-two]
[Enhancement #3 Narrative: Databases][enhance-three]
[Further Enhancements: Security, Interface, and Polishing][enhance-more]
[Course Objectives and Outcomes][course-outcomes]

 #### Enjoy!


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
[enhancement-plan]: https://lumutek.github.io/capstone/narratives/2023/06/11/CodeReview.html
[enhance-one]: https://lumutek.github.io/capstone/narratives/2023/06/12/Enhancement1.html
[enhance-two]: https://lumutek.github.io/capstone/narratives/2023/06/13/Enhancement2.html
[enhance-three]: https://lumutek.github.io/capstone/narratives/2023/06/14/Enhancement3.html
[enhance-more]: https://lumutek.github.io/capstone/narratives/2023/06/15/EnhanmentsX.html
[course-outcomes]: https://lumutek.github.io/capstone/narratives/2023/06/16/CourseOutcomes.html
[code-review]: https://youtu.be/fjA3YFZK3E8

