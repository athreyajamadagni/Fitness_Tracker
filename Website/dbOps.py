from itertools import count
from matplotlib.collections import Collection

collection = None

def __get_database():
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = #insert mongodb atlas url to your database
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['PESUFitness']

def create_new_student(Roll_Number):
    SRN=Roll_Number.upper()
    new_student = {
        "_id" : SRN,
        "Number_of_squats" : 0
               
        }
    collection.insert_one(new_student)

def increment_number_of_squats(Roll_Number,change_of_count):
    SRN=Roll_Number.upper()
    collection.update_one({"_id":SRN},{"$inc":{"Number_of_squats":change_of_count}})
    


def delete_student(Roll_Number):
     SRN=Roll_Number.upper()
     collection.delete_one({"_id":SRN})

def fetch_student(Roll_Number):
    SRN=Roll_Number.upper()
    student = collection.find_one({"_id":SRN})
    print(student)
    return student

def fetch_only_student(Roll_Number):
    SRN=Roll_Number.upper()
    student = fetch_student(SRN)
    if (student!=None):
        return True
    else:
        return False

def fetch_only_count(Roll_Number):
    SRN=Roll_Number.upper()
    student = collection.find_one({"_id":SRN},{'_id': 0, 'Number_of_squats': 1 })
    count= str(student)
    count=count.replace("{'Number_of_squats': ",'')
    count=count.replace("}","")
    #print(count)
    return count



def initialise_data_base(collection_name):
    dbname = __get_database()
    global collection
    collection = dbname[collection_name]