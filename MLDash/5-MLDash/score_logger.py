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
#Win criteria set lower than is tyically seen, for testing and lower memory requirements (try 200 instead, if you've got the hardware) 
AVERAGE_SCORE_TO_SOLVE = 20 # 200
#This is the buffer size for storing consecutive runs, and is central to calculating am moving average of scores, the local minimum score, and the local maximum score.It also ensures that the model can't solve the problem by having a lucky streak
CONSECUTIVE_RUNS_TO_SOLVE = 40 #100
  
  
class ScoreLogger:  
  
    def __init__(self, env_name):  
        self.scores = deque(maxlen=CONSECUTIVE_RUNS_TO_SOLVE)  
        self.env_name = env_name  
        self.metrics_header = ['session', 'run', 'meanScores', 'maxScores', 'globalMax', 'alpha', 'gamma', 'exploreRate', 'batchSize', 'bufferSize']
        self.summary_header = ['session', 'totalRuns', 'totalSteps', 'globalMax', 'alpha', 'gamma', 'epsilonMin', 'epsilonMax', 'epsilonDecay', 'episodes', 'batchSize', 'bufferSize']
        self.metrics_file = METRICS_CSV_PATH
        self.summary_file = SUMMARY_CSV_PATH
        self.toCsv1 = {}
        self.toCsv2 = {}
        self.maxMean = 0
        self.maxScoreGlobal = 0
        

        if os.path.exists(METRICS_CSV_PATH):  
            os.remove(METRICS_CSV_PATH)  
        if os.path.exists(SUMMARY_CSV_PATH):  
            os.remove(SUMMARY_CSV_PATH)
  
    def add_record(self, session, steps, run, exploreRate, gamma, alpha, batchSize, memSize):  
        #An inverted explore rate makes more intuitive sense, especially on data visualization charts
        self.exploreRate_percent = 100*exploreRate
        self.scores.append(steps)  
        self.meanScore = mean(self.scores)
        minScore = min(self.scores)
        maxScore = max(self.scores)
        if (self.maxScoreGlobal < maxScore):
            self.maxScoreGlobal = maxScore
        if (self.maxMean < self.meanScore):
            self.maxMean = self.meanScore
       
        print ("Run: " + str(run) + ", exploration percent: " + str(self.exploreRate_percent) + ", score: " + str(steps)) 
        print ("Scores: (Minimum Score: " + str(minScore) + " MovingAvg: " + str(self.meanScore) + ", MaxAvg: " + str(self.maxMean) + ", LocalMaxScore: " + str(maxScore) + ", GlobalMaxScore: " + str(self.maxScoreGlobal) + ")\n") 
        
        self.toMetricsCsv = {'session' : session, 'run': run, 'meanScores': self.meanScore, 'maxScores': maxScore, 'globalMax': self.maxScoreGlobal, 'alpha': alpha, 'gamma': gamma, 'exploreRate': self.exploreRate_percent, 'batchSize': batchSize, 'bufferSize': memSize}
        
        self._save_csv(self.metrics_file, self.toMetricsCsv, self.metrics_header)
        
        if self.meanScore >= AVERAGE_SCORE_TO_SOLVE and len(self.scores) >= CONSECUTIVE_RUNS_TO_SOLVE:
            return True  
        
        else:
            return False
    
    #While the current implementation does not read the summary data to the dataframe, the program still collects it in the summary.csv file and summary database collection.                       
    def add_summary(self, session, totRuns, totSteps, alpha, gamma, epsMin, epsMax, epsDecay, numEps, batchSize, memSize):   
        print("Cartpole solved in " + str(totRuns) + " runs, with an average score of " + str(self.meanScore) + " and a maximum score of " + str(self.maxScoreGlobal)+ "\n")
        print ("Session Summary:" + "\n Total Runs: " + str(totRuns) + "\n Total steps: " + str(totSteps) + "\n Maximum Score: " + str(self.maxScoreGlobal) + "\n Learning Rate: " + str(alpha) + "\n Discount Factor: " + str(gamma) + "\n Exploration Minimum: " + str(epsMin) + "\n Exploration Maximum: " + str(epsMax) + "\n Exploration Decay: " + str(epsDecay) +"\n # of Episodes: " + str(numEps) + "\n Batch Size: " + str(batchSize) + "\n Buffer Size: " + str(memSize) ) 

        self.toSummaryCsv = {'session' : session, 'totalRuns': totRuns, 'totalSteps': totSteps, 'globalMax': self.maxScoreGlobal, 'alpha': alpha, 'gamma': gamma, 'epsilonMin': epsMin, 'epsilonMax': epsMax, 'epsilonDecay': epsDecay, 'episodes': numEps, 'batchSize': batchSize, 'bufferSize': memSize}
        
        self._save_csv(self.summary_file, self.toSummaryCsv, self.summary_header)
   
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
            
        
            
     

