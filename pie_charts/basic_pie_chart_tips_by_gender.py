### Case study Distribution of tips by gender

import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/tips.csv")

plot = px.pie(
    data_frame=df,
    values='tip',
    names='sex',
    title="Case study Distribution of tips by gender"
    
)

plot.show()