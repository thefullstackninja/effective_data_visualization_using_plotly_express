import plotly.express as px
import pandas as pd

# load data
df = pd.read_csv("../data/clean_auto_mpg.csv")

print(df.columns)
print(df.shape)


plot = px.violin(data_frame=df,
                 x='origin',
                 y='mpg',
                 color='origin',
                 points='all',
                 box=True,
                 hover_name='car name',
                 title='Violinplot for MPG values across cars made from 3 different continents'
                 )

plot.show()
