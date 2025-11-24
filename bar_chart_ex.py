import plotly.express as px
import pandas as pd

data= {
    'Batsman': ['R Sharma', 'V Kohli', 'S Dhavan', 'MS Dhoni', 'D Warner', 'S Raina'],
    '2016': [489, 973, 501, 284, 848, 399],
}

df = pd.DataFrame(data)

fig = px.bar(df, x='Batsman', y='2016')
fig.update_layout(
    title_text='Batsman Runs Analysis (2016)',
    xaxis_title='Batsman Name',
    yaxis_title='Runs',
    title_x=0.5 # Center the Title horizontaly
)

fig.show()