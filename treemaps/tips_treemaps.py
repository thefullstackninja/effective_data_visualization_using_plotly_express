import plotly.express as px
import pandas as pd


df = pd.read_csv("../data/tips.csv")

plot = px.treemap(
    data_frame=df,
    values='tip',
    path = ['time','smoker','sex','day',],
    title="Distribution of tips across the different categorical variables."


)


plot.show()