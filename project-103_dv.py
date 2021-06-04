import pandas as pd
import plotly.express as px

df = pd.read_csv("project-data-1.csv")
scatterGraph = px.scatter(df, x= "cases", y = "country", color="country", size_max = 60)
scatterGraph.show()