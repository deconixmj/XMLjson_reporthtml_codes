# from Extract_data_f import *
# from Extract_data_f1 import *
# # from Extract_data_f2 import *
# # import Extract_data_f2
# # from Extract_data_f2 import vtsongsi_data_1295,vtsongsi_data_1293,EH
# from Extract_data_f2 import *
# from Extract_data_f3 import *
# from Extract_data_f4 import *


from yattag import *
from Data_extract_xts import *
import os

# global EH

print("Execution sprint:")
wave = "Wave22"
start = "04/11/2020"
end = "04/17/2020"
regions = ['000', '001', '002', '003', '004', '005']
device = {'1293': 10, '1295': 10}
final_report = 'xts_report_V2.html'
f = open(final_report, 'w')
# doc, tag, text = Doc(defaults={'color':'red'}).tagtext()
doc, tag, text = Doc().tagtext()

with tag('html'):
    doc.attr(style="background-color:Tomato; padding:50px")
    doc.attr(border="border-color:black;border-width:1px;border-style:solid;")

    with tag('h1'):
        doc.attr(style="text-align:center")
        text('XTS report snapshot ' + '(' + wave + ')' + '\n')

    with tag('body'):
        with tag('h3'):
            text('Environment:')
        with tag('p'):
            text('Start Date:' + start)
            with tag('br'):
                text('End Date:' + end)
        with tag('p'):
            text('DUT:')
            with tag('br'):
                text('1293-->' + str(device['1293']) + " " + "devices")
            with tag('br'):
                text('1295-->' + str(device['1295']) + " " + "devices")


def all_xts(xtspath):
    mypath=xtspath
    xtsname=os.path.split(mypath)
    with tag('h3'):
        text(xtsname[1])
    with tag('table'):
        doc.attr(style="background-color:LightGray;")
        doc.attr(border="1px solid black;")
        with tag('tr'):
            with tag('th'):
                text('Device Model')
            with tag('th'):
                text('Regions')
            with tag('th'):
                text('Fingerprint')
            with tag('th'):
                text('Failed_TC')

            # with tag('th'):
            #     text('Failed_TC')
            with tag('th'):
                text('Modules done/Modules Total')



        if xtsname[1]=="GTS":
            ## 1293
            with tag('tr'):
                with tag('td'):
                    doc.attr(rowspan="7")
                    text('1293')
            for r in regions:
                # gts_data_1293(r,path)
                data4 = gts_data_1293(r, mypath)
                if len(data4) == 0:
                    print("File not found for".format(r))
                    with tag('tr'):
                        with tag('td'):
                            # doc.attr(colspan="4")
                            text(r)
                        with tag('td'):
                            doc.attr(colspan="3")
                            text("File not uploaded")
                    # raise FileNotFoundError
                    continue

                else:
                    with tag('tr'):
                        with tag('td'):
                            text(r)
                        with tag('td'):
                            text(data4[0])
                        with tag('td'):
                            text(data4[1])
                        with tag('td'):
                            text(data4[2])


            #1295
            with tag('tr'):
                with tag('td'):
                    doc.attr(rowspan="7")
                    text('1295')
            for r in regions:
                # gts_data_1295(r,path)
                data5 = gts_data_1295(r, mypath)
                if len(data5) == 0:
                    print("File not found for".format(r))
                    with tag('tr'):
                        with tag('td'):
                            # doc.attr(colspan="4")
                            text(r)
                        with tag('td'):
                            doc.attr(colspan="3")
                            text("File not uploaded")
                    # raise FileNotFoundError
                    continue
                # data5 = vtsongsi_data_1295(r)
                else:
                    with tag('tr'):
                        with tag('td'):
                            text(r)
                        with tag('td'):
                            text(data5[0])
                        with tag('td'):
                            text(data5[1])
                        with tag('td'):
                            text(data5[2])


        else:
            #1293
            with tag('tr'):
                with tag('td'):
                    doc.attr(rowspan="7")
                    text('1293')

            for r in regions:
                data4 = xts_data_1293(r,mypath)
                if len(data4) == 0:
                    print("File not found for".format(r))
                    with tag('tr'):
                        with tag('td'):
                            # doc.attr(colspan="4")
                            text(r)
                        with tag('td'):
                            doc.attr(colspan="3")
                            text("File not uploaded")
                    # raise FileNotFoundError
                    continue

                else:
                    with tag('tr'):
                        with tag('td'):
                            text(r)
                        with tag('td'):
                            text(data4[0])
                        with tag('td'):
                            text(data4[1])
                        with tag('td'):
                            text(data4[2])

            #  for 1295
            with tag('tr'):
                with tag('td'):
                    doc.attr(rowspan="7")
                    text('1295')
            for r in regions:
                data5 = xts_data_1295(r,mypath)
                if len(data5) == 0:
                    print("File not found for".format(r))
                    with tag('tr'):
                        with tag('td'):
                            # doc.attr(colspan="4")
                            text(r)
                        with tag('td'):
                            doc.attr(colspan="3")
                            text("File not uploaded")
                    # raise FileNotFoundError
                    continue
                # data5 = vtsongsi_data_1295(r)
                else:
                    with tag('tr'):
                        with tag('td'):
                            text(r)
                        with tag('td'):
                            text(data5[0])
                        with tag('td'):
                            text(data5[1])
                        with tag('td'):
                            text(data5[2])

    # f.write(doc.getvalue())

rpath="C:\\Aut_review"
xts=os.listdir(rpath)
# print(xts)
for i in xts:
    # if i=="GTS":
    #     print("GTS not implemented yet")
    #     continue
    path=os.path.join(rpath,i)
    all_xts(path)
    # f.write(doc.getvalue())
    print(i+" data done")

f.write(doc.getvalue())
print("All done")







