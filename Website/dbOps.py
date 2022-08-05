from itertools import count
from matplotlib.collections import Collection
from tkinter import *

collection = None

def __get_database():
    from pymongo import MongoClient

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = #insert mongodb atlas url to your database
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['Cluster Name'] #Insert Cluster name

#Creates a new entry into the data base with _id as the roll number
def create_new_student(Roll_Number):
    SRN=Roll_Number.upper()
    new_student = {
        "_id" : SRN,
        "Number_of_squats" : 0
               
        }
    collection.insert_one(new_student)

#Adds the new count to the previous number of squats
def increment_number_of_squats(Roll_Number,change_of_count):
    SRN=Roll_Number.upper()
    collection.update_one({"_id":SRN},{"$inc":{"Number_of_squats":change_of_count}})
    

#Used to delete a certain _id from the cluster
def delete_student(Roll_Number):
     SRN=Roll_Number.upper()
     collection.delete_one({"_id":SRN})

#Used to fetch the _id and number of squats performed by that _id from the database
def fetch_student(Roll_Number):
    SRN=Roll_Number.upper()
    student = collection.find_one({"_id":SRN})
    print(student)
    return student

#Used to fetch only _id from the database
def fetch_only_student(Roll_Number):
    SRN=Roll_Number.upper()
    student = fetch_student(SRN)
    if (student!=None):
        return True
    else:
        return False

#Used to fetch only number of squats performed by that _id from the database
def fetch_only_count(Roll_Number):
    SRN=Roll_Number.upper()
    student = collection.find_one({"_id":SRN},{'_id': 0, 'Number_of_squats': 1 })
    count= str(student)
    count=count.replace("{'Number_of_squats': ",'')
    count=count.replace("}","")
    #print(count)
    return count


#Used to initialize the database
def initialise_data_base(collection_name):
    dbname = __get_database()
    global collection
    collection = dbname[collection_name]

