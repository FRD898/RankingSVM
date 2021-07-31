import pandas as pd
import numpy as np
import pickle

def joinData():     
    data = data2 = data3 = data4 = data5 = data6 = ""
    # Reading data from file1
    with open("../data/Ohsumed/ohsumed.87.txt") as fp:
        data = fp.read()
    
    # Reading data from file2
    with open("../data/Ohsumed/ohsumed.88.txt") as fp:
        data2 = fp.read()
    
    with open("../data/Ohsumed/ohsumed.89.txt") as fp:
        data3 = fp.read()

    with open("../data/Ohsumed/ohsumed.90.txt") as fp:
        data4 = fp.read()
    
    with open("../data/Ohsumed/ohsumed.91.txt") as fp:
        data5 = fp.read()
    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2 
    data += "\n"
    data += data3 
    data += "\n"
    data += data4
    data += "\n"
    data += data5  
    
    with open ("../data/Ohsumed/ohsumed.txt", 'w') as fp:
        fp.write(data)

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

def readQueries():
    '''
    Cargar las consultas desde el archivo que las contiene 
    salida: lista de queries(string)
    '''
    queries = []
    with open("../data/Ohsumed/queries2.txt","r") as f:
        num_lineas = 0
        query = {}
        for line in f:
            num_lineas+=1
            if num_lineas==1:
                query["I"] = line.strip().split(" ")[1]   #ID del query
            elif num_lineas==3:
                query["B"] = line.strip()   #informacion del paciente
            elif num_lineas==5:
                query["W"] = line.strip()   #query
                queries.append(query)
                query = {}
                num_lineas = 0
    return np.array(queries)

def readDocuments():
    '''
    Cargar los documentos desde el archivo que contiene todos los documentos
    salida: lista de documentos(diccionarios)
    '''
    documentos = []
    with open("../data/Ohsumed/ohsumed.txt","r") as f:
        num_lineas = i = 0
        documento = {}
        w = True
        a = True
        for line in f:
            num_lineas+=1
            if num_lineas==1:
                #print(line.strip().split(" "))
                documento["I"] = line.strip().split(" ")[1] #ID del documento
            elif num_lineas==3:
                documento["U"] = line.strip()   #identificador Medline 
            elif num_lineas==5:
                documento["S"] = line.strip()   #fuente
            elif num_lineas==6:
                if ".M" not in line:
                    documento["M"] = " "
                    num_lineas=8   
            elif num_lineas==7:
                documento["M"] = line.strip()   #terminos relacionados
            elif num_lineas==9:
                documento["T"] = line.strip()   #titulo
            elif num_lineas==11:
                documento["P"] = line.strip()   #tipo de publicacion
            elif num_lineas ==12:
                if ".W" not in line:
                    w = False
                    if ".A" not in line:
                        a = False
                        documento["W"] = " "   #autor
                        documento["A"] = " "  #autor
                        documentos.append(documento)
                        documento = {}
                        documento = {"I":line.strip().split(" ")[1]} 
                        num_lineas = 1
                    else:
                        a =True
                else: 
                    w = True
            elif num_lineas==13: 
                if w:
                    documento["W"] = line.strip()   #resumen
                else:
                    documento["W"] = " "   #autor
                    documento["A"] = line.strip()   #autor
                    documentos.append(documento)
                    documento = {}
                    num_lineas = 0
            elif num_lineas==14:
                if ".A" not in line:
                    a = False
                    documento["A"] = " "  #autor
                    documentos.append(documento)
                    documento = {}
                    documento = {"I":line.strip().split(" ")[1]} 
                    num_lineas = 1
            elif num_lineas==15:
                    documento["A"] = line.strip()   #autor
                    documentos.append(documento)
                    documento = {}
                    num_lineas = 0
    print("Se ha leido: ",len(documentos))
    return np.array(documentos)

def saveDocuments(docs):
    '''
    Metodo para guardar cada documento dentro de un archivo .pkl
    input: docs, lista de documentos, cada documentos es un diccionario
    '''
    i = 0
    for doc in docs:
        name = "../docs/"+doc["I"]+".pkl" 
        i+=1
        print(i)
        with open(name,"wb") as f:
            pickle.dump(doc,f,pickle.HIGHEST_PROTOCOL)
            """ f.write(doc["I"]+"\n")
            f.write(doc["U"]+"\n")
            f.write(doc["S"]+"\n")
            f.write(doc["M"]+"\n")
            f.write(doc["T"]+"\n")
            f.write(doc["W"]+"\n")
            f.write(doc["A"]+"\n") """

def readDocument(doc_id):
    name = "../data/docs/"+str(doc_id)+".pkl"
    doc = {}
    with open(name, 'rb') as f:
        doc = pickle.load(f)
    return doc

