from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
# Initializing the MongoClient. This helps to 
# access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:55393/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']


    # Create method to implement the C in CRUD.
    def create(self, data):
        #definition criteria provided, else throw exception
        if data is not None:
            #Make sure that the data parameter is of type dict, insert acceptable data into database
            if isinstance(data, dict):
                is_dict = True
                self.database.animals.insert(data)
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
                cursor = self.database.animals.find(data, {"_id": False})
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
                data = self.database.animals.find_one(data)
                           
            else: 
                raise TypeError("The data entered is not of type dictionary")
                data = False
        else:
            raise Exception("Nothing to read, because data parameter is empty")
            data = False
        return date

            #function that performs the U in CRUD; will accept ANY valid search query and update using _id
    def update(self, lookup, updateData):
        if lookup is not None:
            if isinstance(lookup, dict):
                ident = self.database.animals.find_one(lookup)
                revision = ident.get('_id')
                
                if updateData is not None:
                    if isinstance(updateData, dict):
                        self.database.animals.update_one({"_id" : revision},{"$set": updateData})
                        updated = self.database.animals.find_one({"_id" : revision})
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
                ident = self.database.animals.find_one(lookup).get('_id')
                self.database.animals.delete_one({'_id' : ident})
                return False
            else:
                return True
                raise  TypeError("The lookup data entered is not of type dictionary") 
        else:
            return True
            raise Exception("Nothing to read, because the lookup data parameter is empty")
               

