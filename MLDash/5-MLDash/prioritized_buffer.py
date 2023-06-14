from collections import namedtuple, deque
import random
import numpy as np

Experience = namedtuple('Experience', 'state action reward next_state terminal priority')

class PrioritizedBuffer:
# Initialize a prioritized replay buffer with given buffer size and hyperparameters 
    def __init__(self, batch_size, buffer_size, alpha=0.6, beta=0.6):
        # Create a deque object to store transitions with maximum length of buffer_size
        self.buffer = deque(maxlen=buffer_size)
        # Hyperparameter for prioritizing high initial error transitions
        self.alpha = alpha
        # Hyperparameter for incorporating importance sampling correction into the gradient 
        self.beta = beta
        # Initialize a numpy array to store the priorities of transitions initially set to zero
        self.priorities = np.zeros((buffer_size,), dtype=np.float32)
          # Initialize an index for assigning priorities and storing transitions
        self.index = 0

    def add(self, state, action, reward, next_state, is_terminal):
        # Calculate the priority for the new transition by selecting the maximum priority of all transitions currently in the buffer (if any), or setting it to 1.0 if the buffer is empty
        priority = max(self.priorities) if self.buffer else 1.0
        # Create a new experience object representing the transition and assign it the calculated priority
        experience = Experience(state, action, reward, next_state, is_terminal, priority)
        # Add the experience to the buffer
        self.buffer.append(experience)
        # Assign the same priority to the corresponding entry in the priorities array
        self.priorities[self.index] = priority
        # Increment the index for the next element in the priorities array, wrapping around if necessary
        self.index = (self.index + 1) % len(self.buffer)
        return

    def get_prioritized_indices(self, batch_size):
        # Compute the sampling probabilities for each transition using their respective priorities and the alpha hyperparameter
        probabilities = self.priorities**self.alpha
        # Normalize the probabilities so they sum to 1
        probabilities /= probabilities.sum()
        # Sample indices from the buffer using the computed probabilities
        indices = np.random.choice(len(self.buffer), batch_size, p=probabilities)
        # Compute the importance-sampling weights for the sampled transitions using their probabilities and the beta hyperparameter
        weights = (len(self.buffer) * probabilities[indices])**(-self.beta)
        # Normalize the weights so they are between 0 and 1
        weights /= weights.max()
        # Return the sampled indices and their corresponding weights
        return indices, weights
  
    def update_priorities(self, indices, td_errors):
        # Updates the priority of the transitions at the given indices
        for i, index in enumerate(indices):
            self.priorities[index] = abs(td_errors[i])
        return

    def __len__(self):
        # Returns the number of transitions in the buffer
        return len(self.buffer)