import plotly.express as px
import pandas as pd

df =pd.read_csv("../data/world_happiness_ranking_2019.csv")

print(df.columns)


plot = px.choropleth(data_frame=df,
                     color='Score',
                     locationmode='country names',
                     locations='Country or region',
                     title="World Happiness Chart for 2019",
                     hover_name='Country or region',

                     )

plot.show()