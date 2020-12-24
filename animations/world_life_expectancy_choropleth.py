import plotly.express as px
import pandas as pd

# load the dataset
df = pd.read_csv("../data/gapminder.csv")

plot = px.choropleth(
    data_frame=df,
    color='lifeExp',
    title='Animation showing changes in life expectancy',
    hover_name='country',
    locationmode='country names',
    locations='country',
    animation_frame='year'
)

plot.show()