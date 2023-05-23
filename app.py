from pymongo import MongoClient
import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import pickle
client = MongoClient('mongodb+srv://arunangshudas:kumkumdi@cluster0.pcgl6xx.mongodb.net/?retryWrites=true&w=majority')
db = client['End_to_End_spam_classification']
collection = db['dataset']
data = list(collection.find())
data=pd.DataFrame(data)
ps=PorterStemmer()
corpus=[]
for i in range(0,len(data)):
    review=re.sub('[^a-zA-Z]',' ',data['messages'][i])
    review=review.lower()
    review=review.split()
    
    review=[ps.stem(word) for word in review if not word in stopwords.words('english')]
    review=' '.join(review)
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=3000)
x = cv.fit_transform(corpus).toarray()
y=pd.get_dummies(data['label'])
y=y.iloc[:,1].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)
model1=GaussianNB()
model1.fit(x_train,y_train)
print("GaussianNB Score is ",model1.score(x_test,y_test))
model2=MultinomialNB()
model2.fit(x_train,y_train)
print("MultinomialNB Score is ",model2.score(x_test,y_test))
filename1 = 'GaussianNB.pkl'
filename2 = 'MultinomialNB.pkl'
with open(filename1, 'wb') as file:
    pickle.dump(model1, file)
with open(filename2, 'wb') as file:
    pickle.dump(model2, file)