import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/gapminder_2007.csv")

plot = px.treemap(
    data_frame=df,
    values='pop',
    path= [ 'continent','country',],
    color='lifeExp',
    title="Treemap showing world population and life expectancy for the 2007 year by continent and country ",
    hover_name='country'

)

plot.show()
