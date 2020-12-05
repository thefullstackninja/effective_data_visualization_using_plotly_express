import plotly.express as px
import pandas as pd

# import dataset
df = pd.read_csv("../data/iris.csv")

print(df.columns)

scatterplot = px.scatter(data_frame=df,
                         x='SepalWidthCm',
                         y='PetalLengthCm',
                         size='PetalWidthCm',
                         title="Plot of Sepal width vs Petal length for the Iris flower using Petal width as the size parameter",
                         color='Species')

scatterplot.show()