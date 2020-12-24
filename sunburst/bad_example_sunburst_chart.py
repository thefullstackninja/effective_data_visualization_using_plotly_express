# bad example of a sunburst chart
import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/gapminder_2007.csv")

plot = px.sunburst(
    data_frame=df,
    values='pop',
    path = ['continent', 'country'],
    title="Bad example of Sunburst showing world population for the 2007 year by continent and country ",
    color='lifeExp',

)

plot.show()
