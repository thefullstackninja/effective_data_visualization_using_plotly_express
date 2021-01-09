import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/vgsales.csv")

plot = px.treemap(
    data_frame=df,
    path=['Platform', 'Genre'],
    values='Global_Sales',
    color='NA_Sales',
    title="Game sales by Genre and  Platform in North America and Globally"
)

plot.show()