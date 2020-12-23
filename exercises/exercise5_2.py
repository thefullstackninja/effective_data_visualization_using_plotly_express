import plotly.express as px
import pandas as pd


df = pd.read_csv("../data/tips.csv")

plot = px.box(
    data_frame=df,
    x='day',
    y='tip',
    color='sex',
    hover_name='time',
    title="Boxplot showing the tips shared across different days based on the gender of the tipper."

)

plot.show()