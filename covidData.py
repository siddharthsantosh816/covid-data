import pandas as pd
import plotly.express as px

file1=pd.read_csv('C:/Users/w/Desktop/Python/csv/Covid_data.csv')




scatterG=px.scatter(data_frame=file1,x='date',y='cases')
scatterG.show()