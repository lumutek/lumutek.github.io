import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId
from score_logger import ScoreLogger
import csv

class MLMongo(object):
    """ CRUD operations for MLDash metrics in MongoDB """

    def __init__(self, username, password):
# Initializing the MongoClient. This helps to access the MongoDB databases and metricss.
        self.connection_string = 'mongodb://' + username + ':' + password + '@localhost:27017/TRAIN?authMechanism=SCRAM-SHA-256'
        self.client = MongoClient(self.connection_string) #client
        self.database = self.client['TRAIN']    #database
        self.metrics = self.database['metrics'] #collection
        self.summary = self.database['summary'] #collection
        
        self.metrics_file = 'metrics.csv'
        self.summary_file = 'summary.csv'
        self.fields_metrics = ['session', 'run', 'meanScore', 'maxScore', 'alpha', 'gamma', 'exploreRate', 'batchSize', 'bufferSize']
        self.fields_summary = ['session', 'totalSteps', 'totalRuns', 'maxScore', 'alpha', 'gamma', 'epsilonMin', 'epsilonMax', 'epsilonDecay', 'episodes', 'batchSize', 'bufferSize']

    # Create method to implement the C in CRUD.
    def create(self, data):
        #definition criteria provided, else throw exception
        if data is not None:
            is_dict = False
            #Make sure that the data parameter is of type dict, insert acceptable data into database
            if isinstance(data, dict):
                is_dict = True
                self.database.metrics.insert(data)
            else: 
                raise TypeError("The data entered is not of type dictionary")
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        #Return boolean indicating whether data parameter type was acceptable
        return is_dict
    
    
    #method that returns a cursor/pointer, pointing to a list of results
    def read_all(self, data):
        #Search criteria provided, else throw exception
        if data is not None:
            #Make sure that the data parameter is of type dict, return the cursor pointing to list
            if isinstance(data, dict):
                cursor = self.database.metrics.find(data, {"_id": False})
                return cursor
            else:
                raise TypeError("The data entered is not of type dictionary")
        else:
            raise Exception("No cursor to return, because data parameter is empty")
            
    
    # Method to implement the R in CRUD.
    def read(self, data):
        #Search criteria provided, else throw exception
        if data is not None:
            #Make sure that the data parameter is of type dict, return the first document found
            if isinstance(data, dict):
                data = self.database.metrics.find_one(data)
                return data          
            else: 
                raise TypeError("The data entered is not of type dictionary")
                data = False
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            data = False
        

            #function that performs the U in CRUD; will accept ANY valid search query and update using _id
    def update(self, lookup, updateData):
        if lookup is not None:
            if isinstance(lookup, dict):
                ident = self.database.metrics.find_one(lookup)
                revision = ident.get('_id')
                
                if updateData is not None:
                    if isinstance(updateData, dict):
                        self.database.metrics.update_one({"_id" : revision},{"$set": updateData})
                        updated = self.database.metrics.find_one({"_id" : revision})
                        return updated
                    else:
                        raise TypeError("The update data entered is not of type dictionary")
                else:
                    raise Exception("Nothing to read, because the update data parameter is empty")
            else:
                raise  TypeError("The lookup data entered is not of type dictionary")
        else:
            raise Exception("Nothing to read, because the lookup data parameter is empty")

            
    #performs the D in CRUD     
    def delete(self, lookup):
        if lookup is not None:
            if isinstance(lookup, dict):
                ident = self.database.metrics.find_one(lookup).get('_id')
                self.database.metrics.delete_one({'_id' : ident})
                return False
            else:
                raise  TypeError("The lookup data entered is not of type dictionary") 
                  
        else:
            raise Exception("Nothing to read, because the lookup data parameter is empty")
            
            
            
   #Additional method added to expand CRUD functionality to insert a single document or many documents
    #insert records to the database
    def write_to_metrics(self): #exception handling has been moved to the location of the function call
            with open(self.metrics_file, 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile, fieldnames=self.fields_metrics)
                for row in csvreader:
                    self.metrics.insert_one(row)
            return    
    
    
    def write_to_summary(self): #exception handling has been moved to the location of the function call
            with open(self.summary_file, 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile, fieldnames=self.fields_summary)
                for row in csvreader:
                    self.summary.insert_one(row)
            
     
    #This method allows a user to clear the mongodb backend database 
    def clear_collections(self):
        result = self.database.metrics.delete_many({})
        print(f"{result.deleted_count} documents deleted from {self.metrics} metrics in {self.database} database.")
        result = self.database.summary.delete_many({})
        print(f"{result.deleted_count} documents deleted from {self.summary} metrics in {self.database} database.")
        
    
    