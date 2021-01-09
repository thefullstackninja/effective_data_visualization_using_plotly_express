import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/vgsales.csv")

plot = px.sunburst(
    data_frame=df,
    path=['Platform', 'Genre'],
    values='Global_Sales',
    color='NA_Sales',
    title="Bad Visual Game sales by Genre and  Platform in North America and Globally"
)

plot.show()