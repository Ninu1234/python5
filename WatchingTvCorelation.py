import plotly.express as px
import csv
import numpy as np 
def getDataSource(data):
    iceCreamSales = []
    coldDrinkSales = []
    with open(data)as f:
        df = csv.DictReader(f)
        for row in df:
            iceCreamSales.append(float(row['Size of TV']))
            coldDrinkSales.append(float(row['Average time spent watching TV']))
    return {'x' : iceCreamSales,'y': coldDrinkSales}
def findCorelation(dataSource):
    corelation = np.corrcoef(dataSource['x'],dataSource['y'])
    print(corelation[0,1])
def setup():
    dataPath = 'watchingTv.csv'
    dataSource = getDataSource(dataPath)
    findCorelation(dataSource)
setup()