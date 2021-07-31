from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["localhost"])
""" 
doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"]) """

# retorna un diccionario
#res = es.get(index="ohsumed", id=1) 
#print(res['_source'])

#es.indices.refresh(index="test-index")
body = {
    "query":{
        "multi_match":{
            "query":"Cerebral",
            "fields": ["Title","Abstract","Terms"]
        }
    }
}

res = es.search(index="ohsumed", body = body)
print("Got %d Hits:" % res['hits']['total']['value'])
all_hits = res['hits']['hits']

for num, doc in enumerate(all_hits):
    print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
   
    # Use 'iteritems()` instead of 'items()' if using Python 2
    for key, value in doc.items():
        print (key, "-->", value)
   
    # print a few spaces between each doc for readability
    print ("\n\n")