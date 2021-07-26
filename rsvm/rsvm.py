from sklearn import svm
import pandas as pd
import numpy as np
import sys

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

    return np.asarray(x2), np.asarray(y2)

def getQueryDocumenPair():
    #Leemos el archivo que contiene las etiquetas para cada para documento-consulta 
    df = pd.read_csv('../data/Ohsumed/judged.txt', delimiter = "\t", names=["q_id","d_ui","d_i","r1","r2","r3"])
    
    #Asignamos una puntuacion numérica de 0,1 o 2 a los resultados
    df = df.replace('n', 0)
    df = df.replace('p', 1)
    df = df.replace('d', 2)
    df = df.fillna(0)

    #Creamos una lista donde la i-esima posicion tendrá los documentos de respuesta al query con id i
    list_docs_per_query = [df[df["q_id"]==i] for i in range(1,107)]
    return list_docs_per_query

def readDocuments():
    '''
    Cargar los documentos desde el archivo que contiene todos los documentos
    salida: lista de documentos(diccionarios)
    '''
    with open("../data/Ohsumed/ohsumed.87.txt","r") as f:
        num_lineas = 0
        documento = {}
        documentos = []
        for line in f:
            num_lineas+=1
            if num_lineas==1:
                documento["I"] = line.strip()   #ID del documento
            elif num_lineas==3:
                documento["U"] = line.strip()   #identificador Medline 
            elif num_lineas==5:
                documento["S"] = line.strip()   #fuente
            elif num_lineas==7:
                documento["M"] = line.strip()   #terminos relacionados
            elif num_lineas==9:
                documento["T"] = line.strip()   #titulo
            elif num_lineas==11:
                documento["P"] = line.strip()   #tipo de publicacion
            elif num_lineas==13:
                documento["W"] = line.strip()   #resumen
            elif num_lineas==15:
                documento["A"] = line.strip()   #autor
                num_lineas = 0
                documento = {}
                documentos.append(documento)
    return documentos

def saveDocuments(docs):
    '''
    Metodo para guardar cada documento dentro de un txt
    input: docs, lista de documentos, cada documentos es un diccionario
    '''
    for doc in docs:
        name = doc["I"]+".txt" 
        with open(name,"w") as f:
            f.write(doc["I"]+"\n")
            f.write(doc["U"]+"\n")
            f.write(doc["S"]+"\n")
            f.write(doc["M"]+"\n")
            f.write(doc["T"]+"\n")
            f.write(doc["W"]+"\n")
            f.write(doc["A"]+"\n")

def modelo():
   x2,y2=pair(x,y)
   svc=svm.SVC(kernel='linear').fit(x2,y2)
   return svc

def main():
    #getQueryDocumenPair()
    readDocuments()

if __name__ == "__main__":
    main()
