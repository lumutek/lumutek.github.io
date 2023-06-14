
#Cartpole imports
import gym    
import numpy as np
from score_logger import ScoreLogger 
from dqn_solver import DQNSolver

MAX_RUNS = 3000
MAX_STEPS = 10000
  
class MLCartpole:        
    def __init__(self, a, g, emin, emax, edec, eps, bat, buf):
        self.solved = False
        self.env = "CartPole-v1"
        self.data_file = './metrics.csv'
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
        #BATCH_SIZE specifies how large the prioritized sample is during experience recall batch processing
        self.batch_size = bat
        #BUFFER_SIZE specifies size of customized queue holding model experience (model intermittently reviews
        #  a prioritized buffer sample of experience data of size BATCH_SIZE, instead of reviewing all experience, to reduce memory  #consumption)
        self.buffer_size = buf
        self.max_runs = MAX_RUNS
        self.max_steps = MAX_STEPS
    
    #cartpole(envName, learnRate, gamma, explMin, explMax, explDecay, numEpisodes, batchSize, memSize)
    def cartpole(self):  
        env = gym.make(self.env, render_mode='human')
        scoreLogger = ScoreLogger(self.env)  
        observation_space = env.observation_space.shape[0]  
        action_space = env.action_space.n  
        dqn_solver = DQNSolver(observation_space, action_space, self.alpha, self.epsilon_max, self.batch_size, self.buffer_size) 
        run = 0   
        #The number of runs is limited to promote model efficiency and prevent memory consumption runaway condition
        while run <= MAX_RUNS:   
            run += 1  
            state = env.reset() 
            #This has been modified to work with the newest version of openai gym (gym v25.2)
            state = np.reshape(state[0], (1, observation_space)) 
            # Each step involves the agent choosing an action based on the observation space, or environment
            step = 0  
            # Limiting the maximum number of steps prevents a very successful model from running interminably.
            # This prevents unnecessary memory use.
            while step < MAX_STEPS:  
                # Each successful step increase the score
                step += 1 
                #This allows the training to be displayed as an animation  
                env.render()  
                # This generates a series of actions based on the sequence of current state
                action = dqn_solver.act(state)  
                # Only the first three members of the tuple are relevant here
                state_next, reward, terminal, _, _ = env.step(action)
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
                    self.solved = scoreLogger.add_record(step, run, dqn_solver.exploration_rate, self.gamma, self.alpha, self.buffer_size, self.batch_size, self.epsilon_max, self.epsilon_min, self.epsilon_decay)  
                    # The numEpisodes value is used to cause intermittent, rather than continuous, experience replay
                    # This means that numEpisodes runs will occur between each experience replay
                    if self.solved == True:
                        return self.solved
                    if (run % self.numEpisodes == 0):
                        # This is the stage where model learns by reflecting on its experiences
                        # Stored experiences are used to update the models q_values (weights)
                        dqn_solver.experience_replay(self.batch_size, self.gamma, self.epsilon_decay, self.epsilon_min, self.buffer_size)
                    break            

    
    
