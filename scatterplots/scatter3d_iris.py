import plotly.express as px
import pandas as pd

# import dataset
df = pd.read_csv("../data/iris.csv")

print(df.columns)

plot = px.scatter_3d(data_frame=df,
                     x='SepalWidthCm',
                     y='PetalLengthCm',
                     z='SepalLengthCm',
                     size='PetalWidthCm',
                     color='Species',
                     title="Plot of Sepal width (x) vs Petal length (y) and sepal length (z) with Peatl width as size parameter" )

plot.show()