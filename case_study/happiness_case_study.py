import pandas as pd
import plotly.express as px


df = pd.read_csv("../data/world_happiness_ranking_2019.csv")
print(df.columns)

plot = px.scatter(data_frame=df,
                  x= 'GDP per capita',
                  y='Score',
                  size='Perceptions of corruption',
                  hover_name= 'Country or region',
                  title="Happiness score vs GDP per capital, using Perceived corruption as a size parameter.")


plot.show()