import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/clean_auto_mpg.csv")

plot = px.scatter(data_frame=df,
    x='mpg',
    y='horsepower',
                  size='displacement',
                  color='origin',
                  facet_col='origin',
                  title="Relationship beween Horsepower and MPG",
                  hover_name='car name'


)

plot.show()