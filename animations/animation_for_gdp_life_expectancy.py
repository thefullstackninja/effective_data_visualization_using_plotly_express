
import plotly.express as px
import pandas as pd

# load the dataset
df = pd.read_csv("../data/gapminder.csv")

plot = px.scatter(
    data_frame=df,
    x='gdpPercap',
    y='lifeExp',
    size='pop',
    hover_name='country',
    title="Plot of GDP per capital vs Life expectancy",
    log_x=True,
    color='continent',
    animation_frame='year'
)

plot.show()