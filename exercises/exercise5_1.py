import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/tips.csv")

plot = px.histogram(
    data_frame=df,
    x='tip',
    facet_col='time',
    facet_row='day',
    color='sex',
    barmode='group',
    title="Distribution of tips across different days, different time of the day and different gender."
)

plot.show()