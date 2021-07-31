""" import sys
sys.path.insert(0, '../')
print(sys.path)
from rsvm import main
main.main()
print("From web")
 """
from elasticClient import search
search.Search("test")