 
import json
import sys
import uuid
import getopt
from elasticsearch import Elasticsearch
 
es=Elasticsearch()
indexname=''
ifile=''
ofile=''
 
try:
    i,j = getopt.getopt(sys.argv[1:],'i:f:o:',["index=","input=","output="])
except getopt.GetoptError:
    print('Usage: pcb_to_es1.py --index=<index_name> --input=<json_file> --output=<formatted_json>')
    sys.exit(2)
 
if len(sys.argv) <= 1:
    print('Usage: pcb_to_es1.py --index=<index_name> --input=<json_file> --output=<formatted_json>')
    sys.exit(2)
 
for opt,arg in i:
 
    if opt in ['-i','--index']:
        indexname=arg
    elif opt in ['-f','--input']:
        ifile=arg
    elif opt in ['-o','--output']:
        ofile=arg
 
#
# print(ifile)
# print(ofile)
 
 
headers={'Content-Type': 'application/json'}
f=open(ifile,'r')
f1=open(ofile,'w')
 
final_data=[]
for i in f:
    x=json.loads(i) # returns a dictionary
    labels_json=json.dumps(x["labels"])
    new_labels1=json.loads(labels_json)
    dict1={}
    for i in new_labels1.split('|,'):
        d1={}
        j=i.replace("|",'')
        k=j.split(':')
        d1[k[0]]=k[1]
        dict1.update(d1)
 
    x.pop('labels')
    x.update(dict1)
    data=json.dumps(x)
    data1=json.loads(data)
    final_data.append(data)
 
 
    r = es.index(index=indexname,doc_type='perfmetrics',id=uuid.uuid4(),body=data)
    print(r)
    #print(r.content)
 
for i in final_data:
    f1.write(i)
    f1.write("\n")

 
