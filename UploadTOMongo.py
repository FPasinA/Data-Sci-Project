from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import pandas as pd

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
papers_collection = db['2023']  


n=202300000
for i in range(2890):
    
    df = pd.read_json(f'Project/2023/{n}')

    df = df['abstracts-retrieval-response']
    df['item'].pop('bibrecord')
    df['cited-count'] = df['coredata']['citedby-count']
    df.drop(['affiliation', 'idxterms', 'language', 'authkeywords'], inplace=True)
    
    output_path = f'test/{n}_1.json'
    df.to_json(output_path)
    with open(f'test/{n}_1.json', 'r') as file:
        papers = json.load(file)

    document = {'_id': n, 'info': papers}
    result = papers_collection.insert_one(document)
    n+=1
    #print(f"Inserted {len(result.inserted_ids)} papers into MongoDB.")
    


'''

# Delete all documents in the collection
result = papers_collection.delete_many({})
print("Number of documents deleted:", result.deleted_count)

'''