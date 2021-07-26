import nltk
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize

def removeStopWords(string="eliminar las palabras vacias como, a un, el"):
    '''
    input: string
    output: list fo words different to stop words
    '''
    stop_words = ['en', 'fuerais', 'tuviésemos', 'muy', 'tenidas', 'estuvieron', 'hemos', 'cuando', 'estuvierais', 'suya', 'nosotras', 'vuestras', 'habrían', 'sentidas', 'eres', 'estéis', 'estábamos', 'fuisteis', 'tendrá', 'o', 'fueran', 'erais', 'estuvieseis', 'sentida', 'ese', 'fuimos', 'habrá', 'las', 'fuese', 'vuestra', 'tengo', 'tendremos', 'sea', 'seáis', 'tuviste', 'tendrías', 'como', 'estos', 'tuvieron', 'sentido', 'hubiera', 'habíamos', 'los', 'sentid', 'entre', 'contra', 'mucho', 'han', 'el', 'al', 'qué', 'teníamos', 'muchos', 'otras', 'nuestros', 'sentidos', 'esos', 'estaríais', 'tuviese', 'tú', 'estáis', 'hayamos', 'este', 'estés', 'estuvieran', 'habrás', 'tengamos', 'sobre', 'a', 'otra', 'y', 'mis', 'tuvieseis', 'e', 'tus', 'he', 'tenía', 'poco', 'son', 'estabas', 'otros', 'hubieron', 'hubieses', 'habían', 'hubiéramos', 'seremos', 'mi', 'hubiesen', 'un', 'nuestro', 'tendrían', 'lo', 'ellas', 'se', 'eso', 'hay', 'es', 'tenida', 'ni', 'fueses', 'serían', 'hayas', 'estaré', 'hubieran', 'estad', 'sin', 'habido', 'seréis', 'nada', 'tengáis', 'él', 'serán', 'ella', 'hayan', 'estuvieras', 'has', 'somos', 'más', 'hayáis', 'esto', 'cual', 'hubiésemos', 'suyos', 'soy', 'desde', 'habría', 'ya', 'algo', 'no', 'quienes', 'estabais', 'tuvimos', 'para', 'estuviésemos', 'tenido', 'tenga', 'hubierais', 'tuvieran', 'estas', 'porque', 'tanto', 'seamos', 'estuviesen', 'nos', 'hube', 'tuvieras', 'estarían', 'todo', 'vuestros', 'será', 'estaríamos', 'pero', 'tuvieses', 'algunas', 'tuve', 'seré', 'suyo', 'estuvieses', 'una', 'tendréis', 'habida', 'fue', 'tenías', 'era', 'les', 'uno', 'tu', 'habidas', 'ellos', 'sería', 'tuyos', 'estuvimos', 'fui', 'algunos', 'de', 'habremos', 'con', 'estoy', 'también', 'estará', 'tened', 'estuviste', 'habríais', 'tuyo', 'estemos', 'estarías', 'sus', 'tuvo', 'hubiste', 'hubisteis', 'os', 'estando', 'quien', 'teníais', 'estado', 'estuvo', 'tuya', 'que', 'mío', 'suyas', 'unos', 'sintiendo', 'habías', 'tienes', 'ha', 'estuviese', 'tendríamos', 'estamos', 'habidos', 'hubieras', 'estaréis', 'tendré', 'fuera', 'están', 'mías', 'sois', 'habéis', 'tuyas', 'estaba', 'ti', 'habré', 'habrías', 'habíais', 'fuesen', 'estuve', 'tengas', 'estaban', 'estados', 'habréis', 'tuviéramos', 'hasta', 'por', 'hubimos', 'hubo', 'tenían', 'vosotras', 'ante', 'vosotros', 'está', 'fueseis', 'habrán', 'fueras', 'seríamos', 'tuviesen', 'donde', 'yo', 'tendrán', 'nosotros', 'estás', 'habríamos', 'fuéramos', 'fueron', 'le', 'serás', 'estaremos', 'esa', 'eran', 'tendría', 'sean', 'estarán', 'la', 'tuviera', 'esté', 'del', 'eras', 'estadas', 'su', 'fuésemos', 'tenemos', 'tenéis', 'todos', 'estar', 'tendríais', 'hubiese', 'esas', 'nuestras', 'serías', 'tendrás', 'mí', 'antes', 'hubieseis', 'tenidos', 'tuvisteis', 'estuviéramos', 'estén', 'tuvierais', 'esta', 'siente', 'me', 'tengan', 'fuiste', 'estarás', 'estuvisteis', 'estuviera', 'estada', 'mía', 'te', 'habiendo', 'durante', 'vuestro', 'estaría', 'sí', 'míos', 'seríais', 'otro', 'seas', 'había', 'haya', 'éramos', 'nuestra', 'tienen', 'tiene', 'teniendo']
    #nltk.download()
    #stop_words = set(stopwords.words('spanish'))
    #print(stop_words)
    words = string.strip().lower().split(" ")
    res = [word for word in words if word not in stop_words]
    print(res)


def getQueryList(query):
    '''
    input: string, search query
    return: list of terms in query
    '''
    q = query.strip().lower().split(" ")
    return q

def getDocList(doc):
    d = doc.strip().lower().split(" ")
    return d


def titleScore(query,doc):
    for q in query:
        print(q)
    pass

def abstractScore():
    pass

def bodyScore():
    pass

def titleAbstractScore():
    pass

def BM25():
    pass

def LMIR():
    pass 

def makeFeature(query,document):
    pass

def main():
    print("feature module")
    query_test = getQueryList("Machine learning")
    print(query_test)
    removeStopWords()

if __name__ == '__main__':
    main()    