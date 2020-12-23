### Bad example of Pie chart

import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/gapminder_2007.csv")


plot = px.pie(
    data_frame=df,
    values='pop',
    names= 'country',
    title='Bad example of Pie chart use case'
)

plot.show()