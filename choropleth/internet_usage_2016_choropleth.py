import pandas as pd
import plotly.express as px

# load in the dataset
df = pd.read_csv("../data/share-of-individuals-using-the-internet.csv")

# extract data for 2016
df_2016 = df[df['Year']==2016]

print(df_2016.shape)
print(df.columns)

plot = px.choropleth(data_frame=df_2016,
                     locations='Country',
                     color='Individuals using the Internet (% of population)',
                     locationmode='country names',
                     hover_name='Country',
                     title="Internet usage across countries of the world as a percentage of the total population in 2016.")

plot.show()