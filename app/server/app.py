import sys
sys.path.insert(0, '../../')
from flask import Flask, jsonify,request
from flask_cors import CORS
from elasticClient import search
import pickle
from sklearn import svm
import pandas as pd
from rsvm import features
import numpy as np

app = Flask(__name__)
CORS(app)
model = pickle.load(open("linearSVC.sav", 'rb'))
#result = model.predict([np.array([0,5,5,0])])
#print(result)

@app.route('/search')
def searchDocs():
    query = request.args.get('query')
    docs = search.Search(query)
    f = features.makeFeaturesServer(query,docs)
    n = len(f)
    for i in range(n):
        for j in range(0, n-i-1):
            if model.predict([np.subtract(f[j] , f[j+1])]) ==1:
                docs[j], docs[j+1] = docs[j+1], docs[j]
    
    res = {
        "docs":docs
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug = True, port = 4000)