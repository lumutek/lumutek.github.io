from statistics import mean  
import matplotlib  
matplotlib.use('Agg')  
import matplotlib.pyplot as plt  
from collections import deque  
import os  
import csv  
import numpy as np  
import csv

 
METRICS_CSV_PATH = "metrics.csv" 
SUMMARY_CSV_PATH = "summary.csv"
# This is the average score that the model needs to achieve to be considered as successful in solving the cartpole problem (difficulty)
AVERAGE_SCORE_TO_SOLVE = 20 #195 
#This is the buffer size for storing consecutive runs, and is central to calculating average score, minimum score, and maximum score
#It also ensures that the model can't solve the problem by being wildly lucky during its first runs
CONSECUTIVE_RUNS_TO_SOLVE = 100 #100
  
  
class ScoreLogger:  
  
    def __init__(self, env_name):  
        self.scores = deque(maxlen=CONSECUTIVE_RUNS_TO_SOLVE)  
        self.env_name = env_name  
        self.metrics_header = ['session', 'run', 'meanScore', 'maxScore', 'alpha', 'gamma', 'exploreRate', 'batchSize', 'bufferSize']
        self.summary_header = ['session', 'totalSteps', 'totalRuns', 'maxScore', 'alpha', 'gamma', 'epsilonMin', 'epsilonMax', 'epsilonDecay', 'episodes', 'batchSize', 'bufferSize']
        self.metrics_file = METRICS_CSV_PATH
        self.summary_file = SUMMARY_CSV_PATH
        self.toCsv1 = {}
        self.toCsv2 = {}
        self.maxScoreGlobal = 0

        if os.path.exists(METRICS_CSV_PATH):  
            os.remove(METRICS_CSV_PATH)  
        #if os.path.exists(SUMMARY_CSV_PATH):  
            #os.remove(SUMMARY_CSV_PATH)
  
    def add_record(self, session, score, run, exploreRate, gamma, alpha, batchSize, memSize):  
        #An inverted explore rate makes more intuitive sense, especially on data visualization charts
        self.exploreRate_percent = 100*exploreRate
        self.scores.append(score)  
        meanScore = mean(self.scores)
        minScore = min(self.scores)
        maxScore = max(self.scores)
        if (self.maxScoreGlobal < maxScore):
            self.maxScoreGlobal = maxScore
       
        print ("Run: " + str(run) + ", exploration percent: " + str(self.exploreRate_percent) + ", score: " + str(score)) 
        print ("Scores: (min: " + str(minScore) + ", avg: " + str(meanScore) + ", max: " + str(maxScore) + ")\n") 
        
        self.toCsv1 = {'session' : session, 'run': run, 'meanScore': meanScore, 'maxScore': maxScore, 'alpha': alpha, 'gamma': gamma, 'exploreRate': self.exploreRate_percent, 'batchSize': batchSize, 'bufferSize': memSize}
        
        self._save_csv(self.metrics_file, self.toCsv1, self.metrics_header)
        
        if meanScore >= AVERAGE_SCORE_TO_SOLVE and len(self.scores) >= CONSECUTIVE_RUNS_TO_SOLVE:
            print("Cartpole solved in " + str(len(self.scores)) + " runs, with an average score of " + str(meanScore))
            return True  
        
        else:
            return False
    
                              
    def add_summary(self, session, totSteps, totRuns, alpha, gamma, epsMin, epsMax, epsDecay, numEps, batchSize, memSize):   
        print ("Session Summary:" + "\n Total steps: " + str(totSteps) + "\n Total Runs: " + str(totRuns) + "\n Maximum Score: " + str(self.maxScoreGlobal) + "\n Learning Rate: " + str(alpha) + "\n Discount Factor: " + str(gamma) + "\n Exploration Minimum: " + str(epsMin) + "\n Exploration Maximum: " + str(epsMax) + "\n Exploration Decay: " + str(epsDecay) +"\n # of Episodes: " + str(numEps) + "\n Batch Size: " + str(batchSize) + "\n Buffer Size: " + str(memSize) ) 

        self.toCsv2 = {'session' : session, 'totalSteps': totSteps, 'totalRuns': totRuns, 'maxScore': self.maxScoreGlobal, 'alpha': alpha, 'gamma': gamma, 'epsilonMin': epsMin, 'epsilonMax': epsMax, 'epsilonDecay': epsDecay, 'episodes': numEps, 'batchSize': batchSize, 'bufferSize': memSize}
        
        self._save_csv(self.summary_file, self.toCsv2, self.summary_header)
        #self._read_csv(self.summary_file) 
        self.maxScoreGlobal = 0
    
    
    def _save_csv(self, path, record, header): 
        try:
            with open(path, "a", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=header)
                if not os.path.isfile(path):
                    writer.writeheader(header)  # write header if file does not exist
                writer.writerow(record)
        except IOError:
            print(f"Could not open file {path}") 
        return
            
        
            
     

