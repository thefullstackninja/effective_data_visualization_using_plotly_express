import plotly.express as px
import pandas as pd

# load the dataset
df = pd.read_csv("../data/iris.csv")

print(df.columns)

plot = px.violin(data_frame=df,
                 x='Species',
                 y='SepalLengthCm',
                 title="Iris Dataset Violinplot for Sepal length in cm",
                 color='Species',
                 box=True,
                 points='all'
                 )

plot.show()