from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd
uri = "url"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
data=pd.read_csv("https://raw.githubusercontent.com/sunnysavita10/Naive-Bayes/main/SpamClassifier-with-ML/sms_spam_data/SMSSpamCollection.csv",sep="\t",header=None,names=["label","messages"])
db = client['End_to_End_spam_classification']
collection = db['dataset']
df = data.to_dict(orient='records')
collection.insert_many(df)