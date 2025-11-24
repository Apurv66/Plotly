import plotly.express as px
import pandas as pd

data = {
    'scores':[45,67,84,35,78,94,78,87,72,82,55,63,42]
}
df = pd.DataFrame(data)

fig = px.histogram(df, x='scores', nbins=4) # by default 5 bins
fig.update_layout(
    title_text='Score Distribution of Student',
    xaxis_title='Score Range',
    yaxis_title='Number of Students',
)
fig.show()