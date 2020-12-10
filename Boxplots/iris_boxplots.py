import pandas as pd
import plotly.express as px

# load the dataset
df = pd.read_csv("../data/iris.csv")

print(df.columns)

plot = px.box(data_frame=df,
              x='Species',
              y='SepalLengthCm',
              title="Iris Dataset Boxplot for Sepal length in cm",
              color='Species',
              )

plot.show()