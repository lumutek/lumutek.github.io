from pymongo import MongoClient
from bson.objectid import ObjectId

class MLDash(object):
    """ CRUD operations for MLDash collection in MongoDB """

    def __init__(self, username, password):
# Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        self.connection_string = 'mongodb://localhost:27017'
    #mongodb://' + username + ':' + password + '@localhost:27017/?authMechanism=SCRAM-SHA-256&authSource=TRAIN
        self.client = MongoClient(self.connection_string)
        self.database = self.client['TRAIN']


    # Create method to implement the C in CRUD.
    def create(self, data):
        #definition criteria provided, else throw exception
        if data is not None:
            #Make sure that the data parameter is of type dict, insert acceptable data into database
            if isinstance(data, dict):
                is_dict = True
                self.database.metrics.insert(data)
            else: 
                raise TypeError("The data entered is not of type dictionary")
                is_dict = False
        else:
            is_dict = False
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
                           
            else: 
                raise TypeError("The data entered is not of type dictionary")
                data = False
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            data = False
        return data

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
                        return updated;
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
                return True
                raise  TypeError("The lookup data entered is not of type dictionary") 
        else:
            return True
            raise Exception("Nothing to read, because the lookup data parameter is empty")
            
   #Additional methods added to expand CRUD functionality to insert a single document or many documents
    #insert a single record
    def write(self, record):
        #written = False;
        if record is not None:
            if isinstance(record, dict):
                #TODO: make sure that the id of the inserted record is not already being used
                ident = self.database.metrics.insertOne(record)
                 #Additional check to ensure that the record was written to the database
                #written = bool(find(record))
                #if written is False:
                    #raise Exception("The record was not successfully written to the database")
                return False
            else:
                return True
                raise TypeError("The record could not be written to the database because is not of type dictionary")
        
        else:
            return True
            raise Exception("The record could not be written to the database because it is empty")
        
       
    
    #insert a multiple records
    def writes(self, records):
        if records is not None:
            if isinstance(records, dict):
                #TODO: make sure that the id of the inserted records are not already being used
                ident = self.database.metrics.insertMany(records)
                return False
            else:
                return True
                raise TypeError("The record could not be written to the database because is not of type dictionary")
        #TODO: Implement find() verification such as what was done in the write() function 
        else:
            return True
            raise Exception("The record could not be written to the database because it is empty")
    
