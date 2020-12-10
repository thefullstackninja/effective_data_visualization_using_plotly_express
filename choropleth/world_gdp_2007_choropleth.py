import plotly.express as px
import pandas as pd

# load in the dataset
df = pd.read_csv("../data/gapminder_2007.csv")

print(df.columns)
print(df.shape)

plot = px.choropleth(data_frame=df,
                     title="Choropleth map showing GDP per capital for countries in the world for the 2007 year.",
                     locations='iso_alpha',
                     locationmode='ISO-3',
                     color='gdpPercap',
                     hover_name='country')

plot.show()