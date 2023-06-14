from collections import deque
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import random

class DQNSolver:  
  
    def __init__(self, observation_space, action_space, explMax, memSize, learnRate): 
        self.exploration_rate = explMax  
        self.action_space = action_space  
        self.memory = deque(maxlen=memSize)  
  
        self.model = Sequential()  
        self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))  
        self.model.add(Dense(24, activation="relu"))  
        self.model.add(Dense(self.action_space, activation="linear"))  
        self.model.compile(loss="mse", optimizer=Adam(learning_rate=learnRate))  
  
    def remember(self, state, action, reward, next_state, done):  
        self.memory.append((state, action, reward, next_state, done))  
  
    def act(self, state):  
        if np.random.rand() < self.exploration_rate:  
            return random.randrange(self.action_space)  
        q_values = self.model.predict(state)  
        return np.argmax(q_values[0])  
  
    def experience_replay(self, batchSize, gamma, explDecay, explMin):  
        if len(self.memory) < batchSize: 
            return  
        batch = random.sample(self.memory, batchSize)  
        for state, action, reward, state_next, terminal in batch:  
            q_update = reward  
            if not terminal:  
                q_update = (reward + gamma * np.amax(self.model.predict(state_next)[0]))  
            q_values = self.model.predict(state)  
            q_values[0][action] = q_update  
            self.model.fit(state, q_values, verbose=0)  
        self.exploration_rate *= explDecay  
        self.exploration_rate = max(explMin, self.exploration_rate) 