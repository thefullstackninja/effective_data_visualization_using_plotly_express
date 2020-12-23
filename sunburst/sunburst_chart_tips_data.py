import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/tips.csv")

plot = px.sunburst(
    data_frame=df,
    values='tip',
    path=['sex', 'day', 'time'],
    title="Sunburst chart showing how the time of the day, day of week and gender of customer affects the amount of tip given"
)

plot.show()


