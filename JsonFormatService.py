import json,os,uuid
 
 
class JsonFormatService:
 
    def __init__(self,filename):
        self.filename=filename
        # self.newfile=newfile
        self.final_data = []
 
    def format_json(self):
        f=open(self.filename)
        # json_data_all=[]
        for i in f:
            x = json.loads(i)  # returns a dictionary
            labels_json = json.dumps(x["labels"])
            new_labels1 = json.loads(labels_json)
            dict1 = {}
            for i in new_labels1.split('|,'):
                d1 = {}
                j = i.replace("|", '')
                k = j.split(':')
                d1[k[0]] = k[1]
                dict1.update(d1)
 
            x.pop('labels')
            x.update(dict1)
            data = json.dumps(x)
            # print(x)
            # data1 = json.loads(data)
            # json.dump(data1,f1,indent=2)// makes the json strings andn file invalid.
            self.final_data.append(data)
 
        # json_data_all.ap
        return self.final_data
 
    def save_new_json(self,newfile,final_data):
        f1 = open(newfile,'w')
        for i in final_data:
            f1.write(i)
            f1.write("\n")
