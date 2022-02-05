import base64
from matplotlib import pyplot as plt
import io
from PIL import Image
import numpy as np
 
 
class GraphService:
    # es = Elasticsearch()
 
    lbl = "PBT_test_sprint1"
 
    def __init__(self):
        pass
 
    def graph_function(self,data,graph_type,ofilename):
        if graph_type=="line-chart":
            im=self.pbt_linechart(data,ofilename)
            return im
        if graph_type=="bar-chart":
            im=self.pbt_barchart(data,ofilename)
            return im
        # if graph_type=="data-table":
        #     self.pbt_datatable(data,ofilename)
 
    def pbt_barchart(self,dforgraph,ofilename):
        # all, y_info = xy_axes()
        y_info=dforgraph["metric"]
        xy_axes=dforgraph["xy_axes"]
 
        x_axis = [i for i in xy_axes.keys()]
        y_axis = [i for i in xy_axes.values()]
 
        plt.figure(figsize=(10,5))
        new_x=[2*i for i in x_axis]
        plt.bar(new_x, y_axis, color='#008000', align='center', width=0.5, label=self.lbl)
 
        plt.xlabel('Public cloud provider')
        plt.ylabel(y_info)
        plt.title('PBT performance testing', pad=20)
        lm = max(y_axis) + 500
        # plt.legend(bbox_to_anchor=(1.04,1),loc="upper left",fontsize="small")
        plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0, fontsize="small")
        # plt.legend(bbox_to_anchor=(0,1.04,1.04,0.2), loc="lower left",borderaxespad=0,fontsize="small")
        plt.ylim(0, lm)
 
        xlocs = [i for i in range(len(y_axis))]
        plt.xticks(xlocs, x_axis, rotation='vertical')
        plt.tick_params(axis='x', which='major', pad=20)
        plt.margins(0.2)
        plt.subplots_adjust(bottom=0.25)
        plt.subplots_adjust(top=0.9)
        # plt.tight_layout()
 
        for index, value in enumerate(y_axis):
            v1 = str(value)
            plt.text(xlocs[index] - 0.25, value + 1, v1)
 
        # plt.show()
        plt.savefig(ofilename, bbox_inches='tight')
        ## return the image as an object, object will generate image
 
        buf=io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.clf()
        return buf
 
    # def pbt_barchart_avg(self, dforgraph):
    #     # all, y_info = xy_axes()
    #     y_info = dforgraph["metric"]
    #     xy_axes = dforgraph["xy_axes"]
    #
    #     x_axis = [i for i in xy_axes.keys()]
    #     y_axis = [i for i in xy_axes.values()]
    #
    #     plt.figure(figsize=(10, 5))
    #     new_x = [2 * i for i in x_axis]
    #     plt.bar(new_x, y_axis, color='#008000', align='center', width=0.5, label=self.lbl)
    #
    #     plt.xlabel('Public cloud provider')
    #     plt.ylabel(y_info)
    #     plt.title('PBT performance testing', pad=20)
    #     lm = max(y_axis) + 500
    #     # plt.legend(bbox_to_anchor=(1.04,1),loc="upper left",fontsize="small")
    #     plt.legend(bbox_to_anchor=(1.05, 0.5), loc="center left", borderaxespad=0, fontsize="small")
    #     # plt.legend(bbox_to_anchor=(0,1.04,1.04,0.2), loc="lower left",borderaxespad=0,fontsize="small")
    #     plt.ylim(0, lm)
    #
    #     xlocs = [i for i in range(len(y_axis))]
    #     plt.xticks(xlocs, x_axis, rotation='vertical')
    #     plt.tick_params(axis='x', which='major', pad=20)
    #     plt.margins(0.2)
    #     plt.subplots_adjust(bottom=0.25)
    #     plt.subplots_adjust(top=0.9)
    #     # plt.tight_layout()
    #
    #     for index, value in enumerate(y_axis):
    #         v1 = str(value)
    #         plt.text(xlocs[index] - 0.25, value + 1, v1)
    #
    #     # plt.show()
    #     plt.savefig('pbt_barchart_avg.jpeg', bbox_inches='tight')
    #     ## return the image as an object, object will generate image
    #
    #     buf = io.BytesIO()
    #     plt.savefig(buf, format="png", bbox_inches='tight')
    #     return buf
 
    def pbt_linechart(self,dforgraph,ofilename):
        '''
 
        :return:
        '''
        y_info = dforgraph["metric"]
        xy_axes = dforgraph["xy_axes"]
 
        # x_axis = [i for i in xy_axes.keys()]
        y_axis = [i for i in xy_axes.values()]
        # print(y_axis)
        plt.figure(figsize=(10, 5))
        plt.title("Performance linechart")
        plt.xlabel("x")
        plt.ylabel(y_info)
        plt.ylim(0, 100)
        # x= np.arange(1,4)
        x = np.linspace(0, 2, 3)
        # x = np.array(xx)
        # # print(x)
        y = np.array(y_axis)
        plt.plot(x, y, linestyle='dashed')
        # plt.show()
 
        plt.savefig(ofilename, bbox_inches='tight')
       ## return the image as an object, object will generate image
 
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.clf()
        return buf
 
 
    def pbt_datatable(self,rowdata,coldata,celldata,ofilename):
        '''
 
        :return:
        '''
 
        cols = ["{}".format(i) for i in coldata]
        rows = ["{}".format(k) for k in rowdata]
        # val3 = [["{}".format(col) for col in data27] for row in col]
        data1=celldata
        celltext = []
        for row in range(len(data1)):
            val9 = np.zeros(len(cols))
            val9 = val9 + data1[row]
            celltext.append([i for i in val9])
 
        fig, ax = plt.subplots()
        # plt.figure(figsize=(5,5))
        ax.set_axis_off()
        table = ax.table(cellText=celltext, rowLabels=rows, colLabels=cols, rowColours=["palegreen"] * 10,
                         colColours=["palegreen"] * 10, cellLoc='center', loc='center')
        # plt.subplots_adjust(right=0.2)
        plt.margins(0.2)
        plt.subplots_adjust(left=0.3, bottom=0.25)
        # plt.subplots_adjust(top=0.9)
 
        ax.set_title('pbt data table', fontweight="bold")
 
        # plt.show()
        plt.savefig(ofilename,bbox_inches='tight')
 
        buf = io.BytesIO()
        plt.savefig(buf, format="png", bbox_inches='tight')
        plt.clf()
        return buf
 
 
 
