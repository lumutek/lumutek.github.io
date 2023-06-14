from collections import deque
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import RMSprop
import random
from prioritized_buffer import PrioritizedBuffer 

# predictible randomness for use in random initialization of cartpole observation space and action space
random.seed(42) #seed for random


#The DQNSolver method contains code for neural netrwork architecture and functionality   
class DQNSolver:  
  
    def __init__(self, observation_space, action_space, alpha, epsilon_Max, batch_size, buffer_size): 
        # the likelyhood of exploration is initialized to the specified maximum 
        self.exploration_rate = epsilon_Max 
        # 'learning rate' determines the granularity of the improvements during cost function minimization
        self.learning_rate = alpha     
        # action space = 2 (left or right)
        self.action_space = action_space                  
        #acts as a memory buffer of a specific size; FIFO, can create low memory condition if too large 
        self.memory = PrioritizedBuffer(batch_size, buffer_size)    
        
        #Neural network archirtecture (number of layers, layer types, and the number of arificial neurons in each layer) how the layers architecture is patterned
        self.model = Sequential()     
        # fully interconnected input layer with 24 neurons
        self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))  
        # fully interconnected input layer with 24 neurons
        self.model.add(Dense(24, activation="relu"))   
        ## linear output in the form of probabilities
        self.model.add(Dense(self.action_space, activation="linear"))    
        ## mean squared error loss function, using the RMSprop optimizer. The Adam optimizer is recommended for greater accuracy, 
        # but RMSprop can require as little as one third of the memory due to the way it stores moving averages. 
        self.model.compile(loss="mse", optimizer=RMSprop(learning_rate=self.learning_rate))     
            
    
    def remember(self, state, action, reward, state_next, terminal):
        #adds this experience tuple to a replay memory buffer, which is used later to sample experiences and train the neural network for Q-value approximation.       
        self.memory.add(state, action, reward, state_next, terminal)  
  
    ## move the cart randomly one way or the other, or use the model's experience to choose 
    def act(self, state):  
        #if a random number is less than the current exploration factor...
        if random.random() < self.exploration_rate:  
        # chose a random action, left or right
            return random.randint(0,1)             
        #If the exploration rate generated is not less than the current exploration rate, then the function uses the neural network model (self.model) to predict the Q-values for each possible action in the given state parameter.
        q_values = self.model.predict(state)  
        # returns the action associated with the highest Q-value, indicating the optimal action to take in the given state, according to the model's current estimation.
        return np.argmax(q_values[0])   
        
    # The experience_replay() function has been upgraded to perform prioritized sampling instead of random sampling. This means that the model learns from experiences that are more likely to significantly affect learning outcomes instead of learning from purely random experiences that may have arbitrary instructional value.
    def experience_replay(self, batch_size, gamma, epsilon_decay, epsilon_min, buffer_size):
        # The model is made to wait until memory has reached capacity before "reflecting" on experiences. Functionally speaking, this allows the model to start the prioritized sampling from a collection of data generated using the maximum exploration factor (epsilon). Over time, data is replaced with data that has progressively lower epsilon values.
        if (len(self.memory.buffer) < buffer_size):
            return
        else:
            print("\n*********************\nExperience Replay\n*********************\n")
            # sample a batch from the buffer using prioritized sampling
            indices, priorities = self.memory.get_prioritized_indices(batch_size)
            batch = [self.memory.buffer[i] for i in indices]
            priorities = np.array(priorities)

            # This code block, and the following for-loop, act to iterate through the batch samples
            states = np.array([transition[0] for transition in batch])
            actions = np.array([transition[1] for transition in batch])
            rewards = np.array([transition[2] for transition in batch])
            next_states = np.array([transition[3] for transition in batch])
            terminals = np.array([transition[4] for transition in batch])
            _s = np.array([transition[5] for transition in batch])
            
            #td_errors stands for "temporal difference" errors, which are used as a measure of how surprising or unexpected a particular experience was for the learning agent.
            td_errors = np.zeros(batch_size)
            
            # For each sample, sample elements are filtered to improve q_values and priotitization of experiences
            for i, (state, action, reward, next_state, terminal, _) in enumerate(batch):
                q_values = self.model.predict(state)
                #element values that lend toward model improvement are used to update q_values
                #for terminal states, the reward is used to update the q_values (effectively a deque push operation)
                
                if terminal:
                    q_update = reward
                    q_values[0][action] = q_update
                
                #otherwise, the model predicts the best next state and multiplies it by a factor of gamma, a hyperparameter that represents how much emphasis is placed on future rewards over immediate rewards. This product is then added to the basic reward and pushed onto the deque.
                else:
                    max_q_value = (reward + gamma * np.amax(self.model.predict(next_state)))
                    q_values[0][action] = max_q_value
                    td_errors[i] = abs(max_q_value - q_values[0][action])
                
                #using the new q_values (equivalent to weights), the model is updated so that it can apply what it has learned     
                self.model.fit(state, q_values, verbose=0)
                
            #clear local batch buffer
            states, actions, rewards, next_states, terminals, _s = [], [], [], [], [], []
            
            #prioritized sampling is based on td_errors
            self.memory.update_priorities(indices, td_errors)  
            #The exploration factor represents the probability that an action will be random
            self.exploration_rate *= epsilon_decay
            self.exploration_rate = max(epsilon_min, self.exploration_rate)
        
        return