import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/vgsales.csv")

plot = px.bar(
    data_frame=df,
    x='Platform',
    y='Global_Sales',
    color='NA_Sales',
    facet_col='Genre',
    barmode='group',
    title="Game sales by Genre and  Platform in North America and Globally"
)

plot.show()