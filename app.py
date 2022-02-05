import logging
import pdb
 
from JsonFormatService import *
from ESIngestService import *
from GraphService import *
from ReportService import *
import os,sys,time
import getopt
from datetime import datetime
 
'''
all servcices are independent of each other.
we will will call each service from run_app.py file.
 
'''
 
logger = logging.getLogger('PCB end-to-end automation')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('output.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
 
 
# its taking the arguments as list.
 
ifile = ""
ofile = ""
indexlist=""
 
try:
    i,j = getopt.getopt(sys.argv[1:],"i:f:o:")
except getopt.GetoptError:
    print('Usage: app.py -i index1,index2,index3 -f file1,file2,file3...fileN -o report_file.pdf')
    sys.exit(2)
if len(sys.argv) <= 1:
    print('Usage: app.py -i index1,index2,index3 -f file1,file2,file3...fileN -o report_file.pdf')
    sys.exit(2)
 
for opt,arg in i:
 
    if opt == '-i':
        indexlist=arg.split(',')
    elif opt == '-f':
        ifile=arg.split(',')
    elif opt =="-o":
        ofile=arg
 
# add the timestamp to indexnames
tn=datetime.now()
ts=tn.strftime("%d%m%y_%H%M%S")
indexlistts=[]
for i in indexlist:
    st=i+"_"+ts
    indexlistts.append(st)
 
logger.info(indexlistts)
 
def convert_data(metric,data):
    my_dict = {}
    for k,v in data.items():
        for k1,v1 in v.items():
            if k1==metric:
                my_dict[k] = v1
    fdata={'metric':metric,'xy_axes':my_dict}
    #print(my_dict)
    return fdata
 
def convert_data_for_table(data):
    mydata = []
    for k, v in data.items():
        L = []
        for k1, v1 in v.items():
            L.append(v1)
            # print(L)
        mydata.append(L)
    mydata1=list(zip(*mydata))
    return mydata1
 
 
metriclist = ['Throughput-internal', 'Throughput-external', 'End to End Runtime', 'proccpu', 'proccpu_mapping','cpu_vuln', 'lscpu']
 
if __name__=='__main__':
 
    newfile = ""
    fp = ""
    dr1=os.getcwd()
    coldata=[]
    dr = os.path.join(os.getcwd()+"/original_json")
    e = ESIngestService()
    count = 0
    data = {}
    newdirname="perf_results_formatted"
    try:
        os.mkdir(os.path.join(dr1,newdirname))
    except FileExistsError:
        logger.info("Formatted json directory exists")
    for i in ifile:
 
        fp = os.path.join(dr, i)
        newfiledirpath=""
        newfilepath=""
        try:
            newfiledirpath=os.path.join(dr1,newdirname)
            newfile = newdirname + str(count) + ".json"
            newfilepath = os.path.join(newfiledirpath, newfile)
            # os.mkdir(newfiledirpath)
        except FileExistsError:
            newfile = newdirname+str(count) + ".json"
            newfilepath=os.path.join(newfiledirpath,newfile)
 
        jobj = JsonFormatService(fp)
        logger.info("Formatting service is running")
        # print("Formatting service is running")
        json_data = jobj.format_json()
        jobj.save_new_json(newfilepath,json_data)
        index=indexlistts[count]
 
        # if e.check_index(index):
        #     logger.info("index existed and deleted")
        # else:
        #     logger.info("index does not exists")
        logger.info("Ingesting data")
        e.ingest_data(json_data,index)
        count += 1
        time.sleep(10)
 
        logger.info("searching index and creating data for plotting from each index is running")
        e1=ESIngestService()
        res_data = e1.search_index(index)
        time.sleep(5)
 
        # print(res_data)
        logger.info("Creating data for the file")
        # pdb.set_trace()
        filename = i.split('.')[0]
        coldata.append(filename)
 
        data[filename] = e1.format_data(res_data)
        # time.sleep(60)
    logger.info(data)
 
    '''
        Graph generation code
    '''
 
    g = GraphService()
    imagelist=[]
    for i in metriclist:
        result = convert_data(i, data)
        # print(result)
        time.sleep(3)
        logger.info("Generating graph is running")
        if i=="Throughput-internal":
            ofilename = "pbt_tp_internal.jpeg"
            im = g.graph_function(result, "bar-chart", ofilename)
            # img=cv2.imread(os.path.join(dr1,ofilename))
            imagelist.append(im)
 
        if i=="Throughput-external":
            ofilename = "pbt_tp_external.jpeg"
            im1 = g.graph_function(result, "bar-chart", ofilename)
            # img1 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im1)
 
        if i=="End to End Runtime":
            ofilename = "pbt_tp_endtoend.jpeg"
            im2 = g.graph_function(result, "bar-chart", ofilename)
            # img2 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im2)
 
        if i=="proccpu":
            ofilename = "proccpu_line.jpeg"
            im3 = g.graph_function(result, "line-chart", ofilename)
            # img3 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im3)
 
        if i=="proccpu_mapping":
            ofilename = "proccpumapping_line.jpeg"
            im4 = g.graph_function(result, "line-chart", ofilename)
            # img4 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im4)
 
        if i=="lscpu":
            ofilename = "lscpu_line.jpeg"
            im5 = g.graph_function(result, "line-chart", ofilename)
            # img5 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im5)
 
        if i=="cpu_vuln":
            ofilename = "cpuvuln_line.jpeg"
            im6 = g.graph_function(result, "line-chart", ofilename)
            # img6 = cv2.imread(os.path.join(dr1, ofilename))
            imagelist.append(im6)
        #
 
 
    # for data table we are using the whole data.
    rowdata=metriclist
    celldata=convert_data_for_table(data)
    ofilename="pbt_datatable.jpeg"
    logger.info("Generating data table graph is running")
    im7=g.pbt_datatable(rowdata,coldata,celldata,ofilename)
    # img7 = cv2.imread(os.path.join(dr1, ofilename))
    imagelist.append(im7)
    # print(imagelist)
    # for i in imagelist:
    #     print(type(i))
 
 
 
    # logger.info("Preparing data for avg throughput values per interface")
    # d1 = e1.data_for_plot_avg(res_data)
    # time.sleep(20)
    # logger.info(d1)
    # g1 = GraphService(d1)
    # time.sleep(3)
    # logger.info("Generating graph for avg throughput values per interface is running")
    # im1 = g1.pbt_barchart_avg(d1)
    # time.sleep(3)
    # im="/home/mjpbt1/PycharmProjects/PBT_codes/e2e/pbt_barchart.jpeg"
 
 
    '''
     Report generation code.
    '''
 
    logger.info("Generate report is running")
    r = GenerateReport(imagelist)
    try:
 
        r.go(ofile)
    except Exception:
        logger.exception("error occured")
    # ofilename= "pbt_hcl1.1.pdf"
 
    logger.info("end-to-end automation complete, report generated")
 
 
 
