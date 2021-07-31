from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["localhost"])

def Search(query):
    body = {
        "query":{
            "multi_match":{
                "query": query,
                "fields": ["Title","Abstract","Terms"]
            }
        }
    }
    res = es.search(index="ohsumed", body = body)
    print("Got %d Hits:" % res['hits']['total']['value'])
    all_hits = res['hits']['hits']
    res = [doc["_source"] for doc in all_hits]
    return res 
    #print(all_hits)
    #for num, doc in enumerate(all_hits):
        #print ("DOC ID:", doc["_id"], "--->", doc, type(doc), "\n")
    #    print(num,"---",doc["_source"])
        #for key, value in doc.items():
        #    print (key, "-->", value)