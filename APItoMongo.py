import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://bigbdatasci:yPCC7tTAaDw3QXZd@books.rcvrq.mongodb.net/?retryWrites=true&w=majority&appName=books"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client['Project']
papers_collection = db['Extra1000']  

with open("openalex_data2023.json", "r") as file:
    data = json.load(file)
    
n = 20231000    

for i in (data["results"]):
    document = {"_id":n, "info":i}
    result = papers_collection.insert_one(document)
    n+=1


#result = papers_collection.delete_many({})
#print("Number of documents deleted:", result.deleted_count)

