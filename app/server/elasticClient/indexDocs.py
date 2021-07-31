from datetime import datetime
from elasticsearch import Elasticsearch
import pickle

es = Elasticsearch()

def readDocument(doc_id):
    name = "../data/docs/"+str(doc_id)+".pkl"
    doc = {}
    with open(name, 'rb') as f:
        doc = pickle.load(f)
    return doc


for i in range(348566):
    documento = readDocument(i+1)
    doc = {
        'ID' : documento['I'],
        'UI' : documento['U'],
        'Terms': documento['M'],
        'Title': documento['T'],
        'Publication Type': documento['P'],
        'Abstract': documento['W'],
        'Author': documento['A'],
        'Source': documento['S'],
        'date': datetime.now()
    }
    res = es.index(index="ohsumed", id=documento['I'], body=doc)
    print(res['result'])
