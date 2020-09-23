import plotly.express as px
import csv
with open('watchingTv.csv')as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = 'Size of TV',y = 'Average time spent watching TV')
    fig.show()

