import pandas as pd
import plotly.express as px

file1=pd.read_csv('C:/Users/w/Desktop/Python/csv/Covid_data.csv')
df=file1
#print(df)

covidG=px.scatter(df,x='date', y='cases', color='country', title='COVID Data Analysis')
covidG.show()
