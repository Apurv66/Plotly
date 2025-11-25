import pandas as pd
import plotly.express as px

data = {
    "hours_studied": [2, 3, 4, 5, 6],
    "exam_score": [50, 60, 65, 70, 80],
    "sleep_hours": [7, 6, 6, 5, 5]
}

df = pd.DataFrame(data)

corr = df.corr()

fig = px.imshow(corr, text_auto=True, title="Heatmap")

fig.show()