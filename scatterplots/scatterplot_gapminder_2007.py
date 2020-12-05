import plotly.express as px
import pandas as pd

# load the dataset
df = pd.read_csv("../data/gapminder_2007.csv")

print(df.columns)

scatterplot = px.scatter(data_frame=df,
                         x='gdpPercap',
                         y= 'lifeExp',
                         size='pop',
                         color='continent',
                         hover_name='country',
                         title="Plot of GDP per capital vs Life expectancy in year 2007",
                         log_x=True
                         )

scatterplot.show()