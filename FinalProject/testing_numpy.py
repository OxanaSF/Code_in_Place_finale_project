
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go


x_values = np.linspace(1950, 2020, 15)
ratio = [112.1, 108.8, 107.5, 106.2, 105.5, 104.9, 104.6, 104.3, 104.2, 103.9, 103.5, 103.6, 103.6, 103.6, 103.7, 122]
y_values = np.array(ratio)
trace2 = go.Scatter(x=x_values, y=y_values,
                   mode='lines+markers', name='lines')
data = [trace2]
layout = go.Layout(title='Line chart')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)












