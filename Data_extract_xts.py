import xml.etree.ElementTree as ET
import os
import glob
import xlrd
from zipfile import *

def xts_data_1293(region,p):

    zipfilename = ""
    xmlfile = ""
    data_1293 = []
    path = p
    resfolder=os.path.join(path,"1293",region, "final_results")

    os.chdir(resfolder)
    for file in glob.glob("*.zip"):
        zipfilename = file

    try:
        with ZipFile(zipfilename, 'r') as fzip3:
            print("file found for {}".format(region))
            fzip3.extractall()
    except FileNotFoundError as err:
        print(f"File not found for {region}-->error code {err}")
        return data_1293

    unzipped_file=zipfilename.split(".z")[0]
    resfolder1=os.path.join(resfolder,unzipped_file)
    lastdir=os.listdir(resfolder1)
    resfolder2=os.path.join(resfolder1,lastdir[0])

    os.chdir(resfolder2)
    for file in glob.glob("*.xml"):
        xmlfile=file

    tree=ET.parse(xmlfile)
    root=tree.getroot()
    for Build in root.findall('Build'):
        fingerprint=Build.get('build_fingerprint')
        data_1293.append(fingerprint)
    for Summary in root.findall('Summary'):
        failed_tc=Summary.get('failed')
        data_1293.append(failed_tc)
        md=Summary.get('modules_done')
        mt=Summary.get('modules_total')
        data_1293.append(md + "/" + mt)

    return data_1293

def xts_data_1295(region,p):

    zipfilename = ""
    xmlfile = ""
    data_1295 = []
    path = p
    resfolder=os.path.join(path,"1295",region, "final_results")

    os.chdir(resfolder)
    for file in glob.glob("*.zip"):
        zipfilename = file

    try:
        with ZipFile(zipfilename, 'r') as fzip3:
            print("file found for {}".format(region))
            fzip3.extractall()
    except FileNotFoundError as err:
        print(f"File not found for {region}-->error code {err}")
        return data_1295

    unzipped_file=zipfilename.split(".z")[0]
    resfolder1=os.path.join(resfolder,unzipped_file)
    lastdir=os.listdir(resfolder1)
    resfolder2=os.path.join(resfolder1,lastdir[0])

    os.chdir(resfolder2)
    for file in glob.glob("*.xml"):
        xmlfile = file

    tree=ET.parse(xmlfile)
    root=tree.getroot()
    for Build in root.findall('Build'):
        fingerprint=Build.get('build_fingerprint')
        data_1295.append(fingerprint)
    for Summary in root.findall('Summary'):
        failed_tc=Summary.get('failed')
        data_1295.append(failed_tc)
        md=Summary.get('modules_done')
        mt=Summary.get('modules_total')
        data_1295.append(md + "/" + mt)

    return data_1295


def gts_data_1293(region,p):
    data_1293 = []
    path = p
    # path = "C:\\Aut_review\\GTS"
    resfolder = os.path.join(path, "1293", region, "final_results")
    os.chdir(resfolder)
    for file in glob.glob('*.xlsx'):
        if file:
            # print(file)
            dataxls = file
            break
    else:
        print("file not present")
        return data_1293

    wb = xlrd.open_workbook(dataxls)
    sheet = wb.sheet_by_name('xts_report')
    sheet.cell_value(0, 0)

    for i in range(sheet.ncols):
        data_1293.append(sheet.cell_value(1, i))

    for n, i in enumerate(data_1293):
        if type(i) is float:
            data_1293[n] = int(i)

    # print(data_1293)
    return data_1293


def gts_data_1295(region,p):
    data_1295 = []
    path = p
    # path = "C:\\Aut_review\\GTS"
    resfolder = os.path.join(path, "1295", region, "final_results")

    os.chdir(resfolder)
    for file in glob.glob('*.xlsx'):
        if file:
            dataxls = file
            break
    else:
        print("file not present")
        return data_1295

    wb = xlrd.open_workbook(dataxls)
    sheet = wb.sheet_by_name('xts_report')
    sheet.cell_value(0, 0)

    for i in range(sheet.ncols):
        data_1295.append(sheet.cell_value(1, i))

    for n, i in enumerate(data_1295):
        if type(i) is float:
            data_1295[n] = int(i)

    # print(data_1295)
    return data_1295
