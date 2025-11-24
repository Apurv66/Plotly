import plotly.express as px
import pandas as pd

data = {
    'year': [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
    'virat': [308, 302, 345, 505, 490, 390, 634, 601],
    'rohit': [288, 325, 378, 408, 365, 507, 439, 512]
}

df = pd.DataFrame(data)

fig = px.line(df, x='year', y='virat', markers=True)

fig.update_layout(
    title_text='Virat Runs Analysis',
    xaxis_title='Year',
    yaxis_title='Runs'
)
fig.show()