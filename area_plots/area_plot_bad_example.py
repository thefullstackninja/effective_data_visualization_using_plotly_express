import plotly.express as px
import pandas as pd

# load the data
df = pd.read_csv("../data/apple_stock_price.csv")

print(df.columns)


plot = px.area(data_frame=df, x='date',
               y=['high','low','close'],
               title='Bad example of Area plot')

plot.show()