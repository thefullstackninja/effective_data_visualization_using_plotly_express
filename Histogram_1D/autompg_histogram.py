import plotly.express as px
import pandas as pd

# load data
df = pd.read_csv("../data/clean_auto_mpg.csv")

print(df.columns)
print(df.shape)

plot = px.histogram(data_frame=df,
                    facet_col='origin',
                    x='mpg',
                    color='origin',
                    title="Distribution of MPG values for vehicles made from 3 different continents.",
                    histnorm='probability density')

plot.show()