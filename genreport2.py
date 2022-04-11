from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph,Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
import json
import pandas as pd

def genrepo(userpath):
    userdata=[]
    with open(userpath,"r")as f:
        jsondata=f.read()
        js_obj=json.loads(jsondata)
        num=len(js_obj)
        for item in range(num):
            (userdata.append(js_obj[str(item)]))
        my_dict=userdata
        df=pd.DataFrame(my_dict)
        print("loading...")
        return df
genrepo("C:\\Users\\USER\\jsonfiles\\Details.json")
if __name__ =="__main__":

    #report_pie=Pie(width=4, height=3)
    report=SimpleDocTemplate("report_trialslog.pdf")
    styles=getSampleStyleSheet()      
    #cdata=report_pie.data=[]
    #clabel=report_pie.labels=[]     
    userpath="C:\\Users\\USER\\jsonfiles\\Details.json"
    '''for name in sorted (userpath):
        cdata.append(userpath[0])
        clabel.append(name)
        print(cdata)
        print(clabel)'''     
              
                   
    #report_chart=Drawing()
    #report_chart.add(report_pie)
    
    report_title= Paragraph("Employees Statistics", styles["h1"])
    r_table_sytle=[("ALIGN", (0,0), (-1,-1), 1, colors.navy),
                   ("LINEABOVE", (0,0),(-1,0),1,colors.navy),
                   ("LINEBELOW", (0,0),(-1,0),1,colors.navy)]
    report_table=Table(data=genrepo(userpath),style=r_table_sytle,hAlign="CENTER")
    report.build([report_title ,report_table])
    print("process done")