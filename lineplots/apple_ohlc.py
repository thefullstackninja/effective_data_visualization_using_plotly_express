import plotly.express as px
import pandas as pd

# load the dataframe
df = pd.read_csv("../data/apple_stock_price.csv")

print(df.columns)

plot = px.line(data_frame=df,
               x='date',
               y=['high', 'open','low','close'],
               title="Apple OHLC data over time")

plot.show()