import plotly.express as px
import csv 
import numphy as np

def getdatasource(datapath):
    coffee=[]
    sleep=[]
    with open(datapath)as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            sleep.append(float(row["sleep in hours"]))
           
            coffee.append(float(row["Coffee in ml"]))
    return{"x":coffee,"y":sleep}

def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print(correlation[0,1])

def setup():
    datapath="cups of coffee vs hours of sleep.csv"
    datasource=getdatasource(datapath)
    findcorrelation(datapath)
setup()