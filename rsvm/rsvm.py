from sklearn import svm
import pandas as pd
import numpy as np
import sys
import features
import pickle
import saveReadFiles
def get_pairs(x, y):
    '''
    Obtiene la resta dos a dos de los documentos de respuesta una query 
    input: x , lista de n vectores caracteristicas 
            y, lista de n etiquetas de relevante o no (1:0) respecto a x 
    output: X2, lista conformada por la resta de vectores 
            Y2, lista conformada por las nuevas etiquetas respecto a X2 (1:-1) 
    '''
    x2 = []
    y2 = []
    i=0
    j=0
    number_docs_in_query = len(x)
    #Form pairs between documents 
    while i < number_docs_in_query:
        j = i + 1
        while j < number_docs_in_query:
            x2.append(np.subtract(x[i], x[j]))
            if y[i] > y[j]:
                y2.append(1)
            else:
                y2.append(-1)
            j = j + 1
        i = i + 1

    return np.array(x2), np.array(y2)

def getFeaturesPairs():
    docs_per_query = saveReadFiles.getQueryDocumenPair()
    #docs = readDocuments()
    queries = saveReadFiles.readQueries()
    x_out = []
    y_out = []
    for pairsQD in docs_per_query:
        #print(pairsQD)
        x = []
        y = []
        for index,pairQD in pairsQD.iterrows():
            #print("pairQD",pairQD)
            q_id = pairQD["q_id"] 
            d_i = pairQD["d_i"] 
            s = pairQD["r1"]
            q = queries[int(q_id)-1]
            d = saveReadFiles.readDocument(int(d_i))
            x.append(features.makeFeatures(q,d))
            y.append(int(s))
        x2,y2 = get_pairs(x,y)
        x_out.append(x2)
        y_out.append(y2)
    return x_out,y_out

def trainModel():    
    x,y= getFeaturesPairs()
    print("x: ",x[:2])
    print("y: ",y[:2])
    print(len(x))
    print(len(y))
    
    X_data = x[0]
    for i in range(1,len(x)):
        X_data = np.concatenate((X_data,x[i]))

    y_data = y[0]
    for i in range(1,len(x)):
        y_data = np.concatenate((y_data,y[i]))
    pd.DataFrame(X_data).to_csv("../data/featuresPairsXtotal.csv")
    pd.DataFrame(y_data).to_csv("../data/featuresPairsYtotal.csv")
    #svc=svm.SVC(kernel='linear').fit(x2,y2)
    #return svc

def main():
    #print(getQueryDocumenPair()[0])
    #saveDocuments(readDocuments())
    svm = trainModel()
    #joinData()

if __name__ == "__main__":
    main()
