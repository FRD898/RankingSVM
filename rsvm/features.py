#import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
import math
import numpy as np
stop_words = [
"i",
"me",
"my",
"myself",
"we",
"our",
"ours",
"ourselves",
"you",
"your",
"yours",
"yourself",
"yourselves",
"he",
"him",
"his",
"himself",
"she",
"her",
"hers",
"herself",
"it",
"its",
"itself",
"they",
"them",
"their",
"theirs",
"themselves",
"what",
"which",
"who",
"whom",
"this",
"that",
"these",
"those",
"am",
"is",
"are",
"was",
"were",
"be",
"been",
"being",
"have",
"has",
"had",
"having",
"do",
"does",
"did",
"doing",
"a",
"an",
"the",
"vand",
"but",
"if",
"or",
"because",
"as",
"until",
"while",
"of",
"at",
"by",
"for",
"with",
"about",
"against",
"between",
"into",
"through",
"during",
"before",
"after",
"above",
"below",
"to",
"from",
"up",
"down",
"in",
"out",
"on",
"off",
"over",
"under",
"again",
"further",
"then",
"once",
"here",
"there",
"when",
"where",
"why",
"how",
"all",
"any",
"both",
"each",
"few",
"more",
"most",
"other",
"some",
"such",
"no",
"nor",
"not",
"only",
"own",
"same",
"so",
"than",
"too",
"very",
"s",
"t",
"can",
"will",
"just",
"don",
"should",
"now",
]

def removeStopWords(string="eliminar las palabras vacias como, a un, el"):
    '''
    input: string
    output: list fo words different to stop words
    '''
    #stop_words_spanish = ['en', 'fuerais', 'tuviésemos', 'muy', 'tenidas', 'estuvieron', 'hemos', 'cuando', 'estuvierais', 'suya', 'nosotras', 'vuestras', 'habrían', 'sentidas', 'eres', 'estéis', 'estábamos', 'fuisteis', 'tendrá', 'o', 'fueran', 'erais', 'estuvieseis', 'sentida', 'ese', 'fuimos', 'habrá', 'las', 'fuese', 'vuestra', 'tengo', 'tendremos', 'sea', 'seáis', 'tuviste', 'tendrías', 'como', 'estos', 'tuvieron', 'sentido', 'hubiera', 'habíamos', 'los', 'sentid', 'entre', 'contra', 'mucho', 'han', 'el', 'al', 'qué', 'teníamos', 'muchos', 'otras', 'nuestros', 'sentidos', 'esos', 'estaríais', 'tuviese', 'tú', 'estáis', 'hayamos', 'este', 'estés', 'estuvieran', 'habrás', 'tengamos', 'sobre', 'a', 'otra', 'y', 'mis', 'tuvieseis', 'e', 'tus', 'he', 'tenía', 'poco', 'son', 'estabas', 'otros', 'hubieron', 'hubieses', 'habían', 'hubiéramos', 'seremos', 'mi', 'hubiesen', 'un', 'nuestro', 'tendrían', 'lo', 'ellas', 'se', 'eso', 'hay', 'es', 'tenida', 'ni', 'fueses', 'serían', 'hayas', 'estaré', 'hubieran', 'estad', 'sin', 'habido', 'seréis', 'nada', 'tengáis', 'él', 'serán', 'ella', 'hayan', 'estuvieras', 'has', 'somos', 'más', 'hayáis', 'esto', 'cual', 'hubiésemos', 'suyos', 'soy', 'desde', 'habría', 'ya', 'algo', 'no', 'quienes', 'estabais', 'tuvimos', 'para', 'estuviésemos', 'tenido', 'tenga', 'hubierais', 'tuvieran', 'estas', 'porque', 'tanto', 'seamos', 'estuviesen', 'nos', 'hube', 'tuvieras', 'estarían', 'todo', 'vuestros', 'será', 'estaríamos', 'pero', 'tuvieses', 'algunas', 'tuve', 'seré', 'suyo', 'estuvieses', 'una', 'tendréis', 'habida', 'fue', 'tenías', 'era', 'les', 'uno', 'tu', 'habidas', 'ellos', 'sería', 'tuyos', 'estuvimos', 'fui', 'algunos', 'de', 'habremos', 'con', 'estoy', 'también', 'estará', 'tened', 'estuviste', 'habríais', 'tuyo', 'estemos', 'estarías', 'sus', 'tuvo', 'hubiste', 'hubisteis', 'os', 'estando', 'quien', 'teníais', 'estado', 'estuvo', 'tuya', 'que', 'mío', 'suyas', 'unos', 'sintiendo', 'habías', 'tienes', 'ha', 'estuviese', 'tendríamos', 'estamos', 'habidos', 'hubieras', 'estaréis', 'tendré', 'fuera', 'están', 'mías', 'sois', 'habéis', 'tuyas', 'estaba', 'ti', 'habré', 'habrías', 'habíais', 'fuesen', 'estuve', 'tengas', 'estaban', 'estados', 'habréis', 'tuviéramos', 'hasta', 'por', 'hubimos', 'hubo', 'tenían', 'vosotras', 'ante', 'vosotros', 'está', 'fueseis', 'habrán', 'fueras', 'seríamos', 'tuviesen', 'donde', 'yo', 'tendrán', 'nosotros', 'estás', 'habríamos', 'fuéramos', 'fueron', 'le', 'serás', 'estaremos', 'esa', 'eran', 'tendría', 'sean', 'estarán', 'la', 'tuviera', 'esté', 'del', 'eras', 'estadas', 'su', 'fuésemos', 'tenemos', 'tenéis', 'todos', 'estar', 'tendríais', 'hubiese', 'esas', 'nuestras', 'serías', 'tendrás', 'mí', 'antes', 'hubieseis', 'tenidos', 'tuvisteis', 'estuviéramos', 'estén', 'tuvierais', 'esta', 'siente', 'me', 'tengan', 'fuiste', 'estarás', 'estuvisteis', 'estuviera', 'estada', 'mía', 'te', 'habiendo', 'durante', 'vuestro', 'estaría', 'sí', 'míos', 'seríais', 'otro', 'seas', 'había', 'haya', 'éramos', 'nuestra', 'tienen', 'tiene', 'teniendo']
    #nltk.download()
    #stop_words = set(stopwords.words('spanish'))
    #print(stop_words)
    words = string.strip().lower().split(" ")
    res = [word for word in words if word not in stop_words]
    return res

def getListOfWordsFromSentence(doc):
    '''
    input: string, search query
    return: list of terms in query
    '''
    d = doc.strip().lower().split(" ")
    return d


def titleScore(query,title):
    '''
    input: query:list, consulta o terminos de búsqueda
            title: list, titulo del documento
    output: int, número total de veces que se repite 
    los términos de query en el título
    '''
    score = 0
    for word in title:
        if word in query:
            score+=1
    return score

def abstractScore(query, abstract):
    '''
    input: query:list, consulta o terminos de búsqueda
            abstract: list, resumen del documento
    output: int, número total de veces que se repite 
    los términos de query en el resumen
    '''
    score = 0
    for word in abstract:
        if word in query:
            score+=1
    return score

def bodyScore():
    pass

def titleAbstractScore(query, title, abstract):
    '''
    calcula el número de veces que se produce una ocurrencia de los
    términos del query en el título y el resumen
    '''
    return titleScore(query, title) + abstractScore(query, abstract)

def relatedTermsScore(query, relatedTerms):
    '''
    input: query, list de los terminos de la consulta
           relatedTerms, los términos relacionados o asociados al documento
    output int, score
    '''
    score = 0
    for word in relatedTerms:
        if word in query:
            score+=1
    return score

def idf(q_i):
    '''
    calcula la frecuencia inversa del documento
    '''
    C = 1000 #num of docs
    n = C - df(q_i) + 0.5
    d = df(q_i) + 0.5
    math.log(n/d)

def df(q_i):
    '''
    calcula la frecuencia en el documento, 
    número de docs que contienen query
    '''
    pass

def BM25():
    pass

def LMIR():
    pass 

def makeFeatures(query,document):
    '''
    input: string , consulta de búsqueda
            document, diccionario que contiene las partes del documento
    output: vector de caracteristicas (np.array)
    '''
    q = removeStopWords(query["W"])
    t_s = titleScore(q,removeStopWords(document["T"]))
    a_s = abstractScore(q,removeStopWords(document["W"]))
    ta_s = titleAbstractScore(q,removeStopWords(document["T"]),removeStopWords(document["W"]))
    r_s = relatedTermsScore(q,removeStopWords(document["M"]))
    return np.array([t_s,a_s,ta_s,r_s], dtype=object)

def makeFeaturesServer(query,docs):
    '''
    input: string , consulta de búsqueda
            document, diccionario que contiene las partes del documento
    output: vector de caracteristicas (np.array)
    '''
    print("document to make feature ============================== \n",docs)
    res = []
    for document in docs:
        q = removeStopWords(query)
        t_s = titleScore(q,removeStopWords(document["Title"]))
        a_s = abstractScore(q,removeStopWords(document["Abstract"]))
        ta_s = titleAbstractScore(q,removeStopWords(document["Title"]),removeStopWords(document["Abstract"]))
        r_s = relatedTermsScore(q,removeStopWords(document["Terms"]))
        res.append([t_s,a_s,ta_s,r_s])
    return np.array(res, dtype=object)

def main():
    print("feature module")
    #query_test = getListOfWordsFromSentence("Machine learning")
    #print(query_test)
    doc = {"T":"prueba de la vida","W":"asn esta es la vida, y la vida tiene pruebas", "M":"psicología de la vida"}
    print(makeFeatures("prueba",doc))
if __name__ == '__main__':
    main()    