import pandas as pd
from pymongo import MongoClient
from bson.objectid import ObjectId
from score_logger import ScoreLogger
import csv

DATA_FILE = "metrics.csv"
class MLMongo(object):
    """ CRUD operations for MLDash collection in MongoDB """

    def __init__(self, username, password):
# Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.connection_string = 'mongodb://localhost:27017/'
    #mongodb://' + username + ':' + password + '@localhost:27017/?authMechanism=SCRAM-SHA-256&authSource=TRAIN
        self.client = MongoClient(self.connection_string) #client
        self.database = self.client['TRAIN']    #database
        self.metrics = self.database['metrics'] #collection
        self.data_file = DATA_FILE
        self.fieldnames = ['run', 'exploreRate', 'score', 'minScore', 'meanScore', 'maxScore', 'gamma', 'alpha', 'memorySize', 'batchSize']
        

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
    #insert multiple records to the database
    def writeDb(self): #exception handling has been moved to the location of the function call
            with open(self.data_file, 'r', newline='') as csvfile:
                csvreader = csv.DictReader(csvfile, fieldnames=self.fieldnames)
                for row in csvreader:
                    self.database.metrics.insert_one(row)
        
    
    