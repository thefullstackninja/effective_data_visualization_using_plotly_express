import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/gapminder_2007.csv")


plot = px.pie(
    data_frame=df,
    values='pop',
    names= 'continent',
    title='World Population by continent in 2007'
)

plot.show()