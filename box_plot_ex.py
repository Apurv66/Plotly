import plotly.express as px
import pandas as pd

df = px.data.tips() # It is a built-in dataset available within Plotly Express

fig = px.box(df, y='total_bill')

fig.show()