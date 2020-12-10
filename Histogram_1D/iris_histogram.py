import pandas as pd
import plotly.express as px

# load the dataset
df = pd.read_csv("../data/iris.csv")

print(df.columns)

plot = px.histogram(data_frame=df,
                    x='SepalLengthCm',
                    title="Distribution of Sepal length in Iris Dataset",
                    facet_col='Species',
                    color='Species')

plot.show()