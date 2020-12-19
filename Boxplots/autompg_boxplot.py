import plotly.express as px
import pandas as pd

# load data
df = pd.read_csv("../data/clean_auto_mpg.csv")

print(df.columns)
print(df.shape)

plot = px.box(data_frame=df,
              x='origin',
              y='mpg',
              color='origin',
              title="Boxplot of MPG values for vehicles from different continents")

plot.show()