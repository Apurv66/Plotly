import plotly.express as px
import pandas as pd

data = {
    'Batsman': ['R Sharma', 'S Gill', 'V Kohli', 'KL Rahul', 'S Iyer', 'A Patel', 'W Sundar'],
    'Runs': [73, 9, 5, 11, 61, 44, 12]
}

df = pd.DataFrame(data)

fig = px.pie(df, values='Runs', names='Batsman', title='Run Contribution Analysis (IND vs AUS)')
fig.update_traces(textinfo='percent+label')

fig.show()