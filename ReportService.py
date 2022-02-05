 
import os
 
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Flowable,Image
from reportlab.platypus import Table,doctemplate,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib import colors
from configparser import ConfigParser
PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
 
config=ConfigParser()
config.read("config.properties")
Title = config.get("main","title")
pageinfo = config.get("main","pageinfo")
 
 
class GenerateReport:
    # self.canvas = canvas
    # self.doc = doc
 
    def __init__(self,iml):
        self.iml=iml
        # self.im1=im1
    #     # self.doc=doc
    #     # self.canvas = None
    #     # self.imgobj=imgobj
    #     self.image_file=image_file
 
 
 
    def myFirstPage(self,canvas,doc):
        self.canvas=canvas
        self.doc=doc
        self.canvas.saveState()
        self.canvas.setFont('Times-Bold', 16)
        self.canvas.drawCentredString(PAGE_WIDTH / 2.0, PAGE_HEIGHT - 108, Title)
        self.canvas.setFont('Times-Roman', 9)
        self.canvas.drawString(inch, 0.75 * inch, "Page %d / %s" % (self.doc.page, pageinfo))
        self.canvas.restoreState()
 
    def myLaterPages(self,canvas,doc):
        self.canvas=canvas
        self.doc=doc
        self.canvas.saveState()
        self.canvas.setFont('Times-Roman', 9)
        self.canvas.drawString(inch, 0.75*inch, "Page %d %s" % (self.doc.page, pageinfo))
        self.canvas.restoreState()
 
    def go(self,filename):
        doc = SimpleDocTemplate(filename)
        Story = [Spacer(1, 2 * inch)]
        styles = getSampleStyleSheet()
        style = styles["Normal"]
        style1 = styles["Heading1"]
 
        width, height = A4
 
        styleN = styles["BodyText"]
        styleN.alignment = TA_LEFT
        styleBH = styles["Normal"]
        styleBH.alignment = TA_CENTER
 
        Story.append(Paragraph("Objective", style1))
        Story.append(Paragraph(config.get("descriptions", "text1"), style))
 
       # f=Flowable
       #  description = Paragraph(config.get("descriptions","text3"), styleN)
       #  description1 = Paragraph(config.get("descriptions","text4"),styleN)
       #  description2 = Paragraph(config.get("descriptions", "text5"), styleN)
       #  description3 = Paragraph(config.get("descriptions", "text6"), styleN)
       #  description4 = Paragraph(config.get("descriptions", "text7"), styleN)
       #  description5 = Paragraph(config.get("descriptions", "text8"), styleN)
       #  description6 = Paragraph(config.get("descriptions", "text9"), styleN)
       #  description7 = Paragraph(config.get("descriptions", "text10"), styleN)
 
        # f = open("/home/mjpbt1/PycharmProjects/PBT_codes/e2e/pbt_barchart.jpeg","rb")
        # f=open(self.image_file)
        count=3
        for i in self.iml:
            # f=os.path.join(os.getcwd(),str(i))
            img = Image(i, width=5 * inch, height=4 * inch)
            # img1 = Image(self.im1, width=5 * inch, height=4 * inch)
            # img_p=Paragraph(img,style)
            # img.hAlign.center(3)
            description = Paragraph(config.get("descriptions", "text"+str(count)), styleN)
 
            data = [[description,img]]
            # data1=[[description1,img1]]
 
            table = Table(data, colWidths = [2.7 * cm, 15 * cm])
 
        # 5 * [0.4 * inch], 4 * [0.4 * inch]
        # colWidths = [2.05 * cm, 2.7 * cm, 5 * cm, 3 * cm, 3 * cm])
 
            table.setStyle(TableStyle([
                ('VALIGN',(0,0),(0,0),'TOP'),
                ('VALIGN',(1,0),(1,0),'TOP'),
                ('GRID', (0, 0), (-1, -1), 2, colors.black),
                ('BOX', (0, 0), (-1, -1), 2, colors.black),
            ]))
 
            # table1 = Table(data1, colWidths=[2.7 * cm, 15 * cm])
 
            # 5 * [0.4 * inch], 4 * [0.4 * inch]
           # colWidths = [2.05 * cm, 2.7 * cm, 5 * cm, 3 * cm, 3 * cm])
 
            # table1.setStyle(TableStyle([
            #     ('VALIGN', (0, 0), (0, 0), 'TOP'),
            #     ('VALIGN', (1, 0), (1, 0), 'TOP'),
            #     ('GRID', (0, 0), (-1, -1), 2, colors.black),
            #     ('BOX', (0, 0), (-1, -1), 2, colors.black),
            # ]))
 
            Story.append(Spacer(1, 1 * inch))
            Story.append(table)
            # Story.append(table1)
            count+=1
 
        doc.build(Story, onFirstPage=self.myFirstPage, onLaterPages=self.myLaterPages)
