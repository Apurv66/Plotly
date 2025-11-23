import plotly.express as px
import pandas as pd

data = {
    'batter': ['V Kohli', 'R Sharma', 'S Dhavan', 'D Warner', 'MS Dhoni', 'R Dravid', 'S Tendulkar', 'A Russal'],
    'Avg': [51, 45, 55, 47, 43, 55, 57, 38],
    'SR': [144.8, 152.3, 139.9, 148.3, 152.9, 122.5, 122.3, 172.1]
}
df = pd.DataFrame(data)
fig = px.scatter(df, x='Avg', y='SR',hover_name="batter")
fig.update_layout(
    title_text="Average vs Strike Rate",
    xaxis_title="Average",
    yaxis_title="Strike Rate"
    
)
fig.show()