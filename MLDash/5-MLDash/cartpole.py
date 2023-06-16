
#Cartpole imports
import gym    
import numpy as np
from score_logger import ScoreLogger 
from dqn_solver import DQNSolver

MAX_RUNS = 3000
MAX_STEPS = 2000
  
class MLCartpole:        
    def __init__(self, session, anim_on, a, g, emin, emax, edec, eps, bat, buf):
        print("Animation Enabled: " + str(anim_on))
        self.solved = False
        self.session = session
        self.env = "CartPole-v1"
        # determines the granularity of the improvements during cost function minimization  
        self.alpha = a
        # "discount rate" correlated to how much the model values future rewards (lower value means more "planning"; 
        # gamma = 1 equivalent to a greedy algorithm) 
        self.gamma = g
        # epsilon determines the ratio of exploration to exploitation. Scales down from max to min at rate (1-epsilon_decay)
        self.epsilon_min = emin
        self.epsilon_max = emax
        self.epsilon_decay = edec
        #EPISODES specifies how many runs the model performs between experience recall batch processing
        self.numEpisodes = eps
        # Each run is composed of steps, and can be thought of as a single attempt to balance the pole
        self.runs = 0
        # Each step involves the agent choosing an action based on the observation space, or environment 
        self.steps = 0
        self.totSteps = 0
        #BATCH_SIZE specifies how large the prioritized sample is during experience recall batch processing
        self.batch_size = bat
        #BUFFER_SIZE specifies size of customized queue holding model experience (model intermittently reviews
        #  a prioritized buffer sample of experience data of size BATCH_SIZE, instead of reviewing all experience, to reduce memory  #consumption)
        self.buffer_size = buf
        self.cart_animation = anim_on
        self.max_runs = MAX_RUNS
        self.max_steps = MAX_STEPS
    
    #cartpole(envName, learnRate, gamma, explMin, explMax, explDecay, numEpisodes, batchSize, memSize)
    def cartpole(self, animation):  
        if animation == True:
            env = gym.make(self.env, render_mode='human')
        else:
            env = gym.make(self.env)
        scoreLogger = ScoreLogger(self.env)  
        observation_space = env.observation_space.shape[0]  
        action_space = env.action_space.n  
        dqn_solver = DQNSolver(observation_space, action_space, self.alpha, self.epsilon_max, self.batch_size, self.buffer_size)
        #The number of runs is limited to promote model efficiency and prevent memory consumption runaway condition
        while self.runs <= self.max_runs:   
            self.steps = 0
            self.runs += 1 
            state = env.reset() 
            #This has been modified to work with a newer version of OpenAI Gym (gym v25.2)
            state = np.reshape(state, (1, observation_space)) 
            
            while self.steps < self.max_steps:  
                # Each successful step increases the score/reward; Limiting the maximum number of steps prevents a very successful model from running interminably (This prevents unnecessary memory use).
                self.steps += 1 
                #This allows the training to be displayed as an animation 
                if animation == True:
                    env.render()  
                # This generates a series of actions based on the sequence of current state
                action = dqn_solver.act(state)  
                # Only the first three members of the tuple are relevant here
                state_next, reward, terminal, _ = env.step(action)
                # If the step limit has been reached, classify as terminal to credit the model with points
                if self.steps == self.max_steps:
                    terminal = True
                # positive reward if succeeding, negative if failed  
                reward = reward if not terminal else -reward  
                # The model predicts what the optimal move will be during the next step
                state_next = np.reshape(state_next, (1, observation_space))  
                # simply adds the combination of state, action, reward, next state, and state of termination to memory 
                dqn_solver.remember(state, action, reward, state_next, terminal)  
                # state is updated to prepare for the next step
                state = state_next  
                   
                # Each time a run ends, scoreLogger saves score and model parameters for database storage
                if terminal:  
                    self.solved = scoreLogger.add_record(self.session, self.steps, self.runs, dqn_solver.explorationRate, self.gamma, self.alpha, self.batch_size, self.buffer_size)  
                    self.totSteps += self.steps
                    if self.solved == True:
                        scoreLogger.add_summary(self.session, self.runs, self.totSteps, self.alpha, self.gamma, self.epsilon_min, self.epsilon_max, self.epsilon_decay, self.numEpisodes, self.batch_size, self.buffer_size)  

                        return self.solved
                    
                    # The numEpisodes value is used to cause intermittent, rather than continuous, experience replay
                    # This means that numEpisodes runs will occur between each experience replay
                    if (self.runs % self.numEpisodes == 0):
                        # This is the stage where model learns by reflecting on its experiences (experience replay)
                        # Stored experiences are used to update the models q_values (deep-Q weights)
                        dqn_solver.experience_replay(self.gamma, self.epsilon_decay, self.epsilon_min)
                    break  
            
    
    
