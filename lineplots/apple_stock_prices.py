import plotly.express as px
import pandas as pd

# load the dataframe
df = pd.read_csv("../data/apple_stock_price.csv")

print(df.columns)

plot = px.line(data_frame=df,
               x='date',
               y='high',
               title="Apple stock prices over time")

plot.show()