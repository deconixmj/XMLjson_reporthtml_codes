import time
 
from elasticsearch import Elasticsearch
import os, uuid
 
class ESIngestService:
    '''
    Ingest json data into elasticsearch index.
    Search index and get the required data,
    Prepare the data for plotting graph
    '''
    es = Elasticsearch()
 
    def check_index(self, index):
        if self.es.indices.exists(index=index):
            self.es.indices.delete(index=index)
 
    def ingest_data(self, json_data, index):
        # data=self.json_data
        for i in json_data:
            self.r = self.es.index(index=index, doc_type='cloudperfmetrics', id=uuid.uuid4(), body=i)
 
   def search_index(self, index):
        # res_all=[]
        # self.res = self.es.search(index=index, body={"query": {"match": {"metric": "Throughput"}}, "size": 20})
        self.res = self.es.search(index=index,body={"query":{"match_all":{}},"size":20})
        # res_all.append(self.res)
        return self.res
 
    def get_data(self,resdata1):
        metriclist = ['Throughput-internal','Throughput-external','End to End Runtime','proccpu','proccpu_mapping','cpu_vuln','lscpu']
        My_Dict = {}
 
        for i in metriclist:
 
            if i=="Throughput-internal":
                m = i.split("-")[0]
                iptype = i.split("-")[1]
 
            elif i=="Throughput-external":
                m = i.split("-")[0]
                iptype = i.split("-")[1]
 
            else:
                m=i
                iptype=""
 
            L = []
            for k in resdata1["hits"]["hits"]:
 
                d = k["_source"]
                if m in d.values() and iptype=="":
                    L.append(d['value'])
                elif m in d.values() and iptype in d.values():
                    L.append(d['value'])
 
            My_Dict[i] = L
            # print(My_Dict)
 
        print(My_Dict)
        return My_Dict
 
    def avg(self,list):
 
        if (len(list))>0:
            avg = sum(list) / len(list)
            return avg
        else:
            print("List is empty")
 
    def format_data(self, resdata):
 
        data = self.get_data(resdata)
 
        for k, v in data.items():
            if k == 'Throughput-internal':
                data[k] = self.avg(v)
            if k == 'Throughput-external':
                data[k] = self.avg(v)
            if k == 'End to End Runtime':
                data[k] = v[0]
            if k == 'proccpu':
                data[k] = min(v)
            if k == 'proccpu_mapping':
                data[k]=min(v)
            if k == 'cpu_vuln':
                data[k]=max(v)
            if k == 'lscpu':
                data[k]=max(v)
            # alldata1.append(i[k])
 
        return data
 
 
