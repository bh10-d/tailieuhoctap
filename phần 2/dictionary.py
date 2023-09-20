def createDic(Max):
    d=dict()
    for i in range(1,Max+1):
        d[i]=i**2
    return d 
def printItem(dict):            
    for k,v in dict.items():
        print(k,v) 
def printKey(dict):
      for k in dict.keys():
        print(k) 
def printValue(dict):
     for v in dict.values():
        print(v) 
