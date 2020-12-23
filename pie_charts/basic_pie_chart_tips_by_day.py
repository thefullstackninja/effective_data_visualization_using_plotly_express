# pie chart showing the percentage of tips gotten by day of the week
import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/tips.csv")


plot = px.pie(
    data_frame=df,
    names='day',
    values='tip',
    title="Percentage of tips gotten by day of the week"
)

plot.show()