
import plotly.express as px
import csv 
import numphy as np

def getdatasource(datapath):
    marks=[]
    days=[]
    with open(datapath)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
           
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def setup():
    datapath="Student Marks vs Days Present.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datapath)
setup()