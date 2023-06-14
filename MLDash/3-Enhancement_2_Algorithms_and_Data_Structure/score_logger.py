from statistics import mean  
import matplotlib  
matplotlib.use('Agg')  
import matplotlib.pyplot as plt  
from collections import deque  
import os  
import csv  
import numpy as np  
import csv


#os.system('set KMP_DUPLICATE_LIB_OK=TRUE') 
METRICS_CSV_PATH = "metrics.csv"   
AVERAGE_SCORE_TO_SOLVE = 180 
CONSECUTIVE_RUNS_TO_SOLVE = 100 
DATA_FILE = "metrics.csv"
  
  
class ScoreLogger:  
  
    def __init__(self, env_name):  
        self.scores = deque(maxlen=CONSECUTIVE_RUNS_TO_SOLVE)  
        self.env_name = env_name  
        self.fieldnames = ['run', 'exploreRate', 'score', 'minScore', 'meanScore', 'maxScore', 'gamma', 'alpha', 'memorySize', 'batchSize']
        self.toCsv2 = {'run': 1, 'explore rate': 0.25, 'score': 17, 'min score': 17, 'mean score': 17, 'max score': 17, 'gamma': 0.9, 'alpha': 0.01, 'memory size': 1200, 'batch size': 12}

        if os.path.exists(METRICS_CSV_PATH):  
            os.remove(METRICS_CSV_PATH)  
  
    def add_record(self, score, run, explore_rate, gamma, alpha, memSize, batchSize, epsilonMax, epsilonMin, epsilonDecay):   
        self.scores.append(score)  
        mean_score = mean(self.scores)
        min_score = min(self.scores)
        max_score = max(self.scores)
        explore_rate = 1 - explore_rate #this allows exploration to be intuitively correlated with performance

        print ("Run: " + str(run) + ", exploration: " + str(explore_rate) + ", score: " + str(score)) 
        print ("Scores: (min: " + str(min_score) + ", avg: " + str(mean_score) + ", max: " + str(max_score) + ")\n") 
        
        #toCsv1 = str(run) + "," + str(explore_rate) + "," + str(score) + "," + str(min(self.scores)) + "," + str(mean_score) + "," + str(max(self.scores)) + "," + str(gamma) + "," + str(alpha) + "," + str(memSize) + "," + str(batchSize) + "," + str(epsilonMax) + "," + str(epsilonMin) + "," + str(epsilonDecay)
        self.toCsv2 = {'run': run, 'exploreRate': explore_rate, 'score': score, 'minScore' : min_score, 'meanScore': mean_score, 'maxScore': max_score, 'gamma': gamma, 'alpha': alpha, 'memorySize': memSize, 'batchSize': batchSize}#, 'epsilonMax': epsilonMax, 'epsilonMin': epsilonMin, 'epsilonDecay': epsilonDecay
        self._save_csv(METRICS_CSV_PATH, self.toCsv2 )
        if mean_score >= AVERAGE_SCORE_TO_SOLVE and len(self.scores) >= CONSECUTIVE_RUNS_TO_SOLVE:  
            self._write_csv(DATA_FILE)   
            return True  
        
        else:
            return False
  
  
    def _save_csv(self, path, record):  
        try:
            with open(path, "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                if not os.path.exists(path):
                    writer.writeheader()
                writer.writerow(record)
        except IOError:
            print(f"Could not open file {path}") 
        return
            
    
    def _write_csv(self, path):
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            self.data = list(reader)
        #self._close_csv(file)
        return
            
     
    def _close_csv(self, file):
        file.close()
        return

