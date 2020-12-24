import plotly.express as px
import pandas as pd

# load the dataset
df = pd.read_csv("../data/all_stocks_5yr.csv")

plot = px.line(data_frame=df,
               x='date',
               y='open',
               animation_frame='Name',
               log_y=True,
               title="Stoc Open prices by company")

plot.show()