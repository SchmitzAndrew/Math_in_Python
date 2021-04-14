import pandas as pd
import plotly
import plotly.graph_objs as go



def multiDScatterPlot():
    col_list = ["age", "freetime", "goout", "studytime"]
    data = pd.read_csv("student-mat.csv",  usecols=col_list)

    markercolor = data['age']

    figure = go.Scatter3d(x=data['freetime'], y=data['goout'],  z=data['studytime'], marker=dict(color=markercolor,opacity=1,reversescale=True,colorscale='Blues',size=5),line=dict (width=0.02), mode='markers')

    layout = go.Layout(scene=dict(xaxis =dict( title="Free Time"), yaxis=dict( title="Go Out"), zaxis=dict( title="Study Time")),)

    plotly.offline.plot({"data": [figure], "layout": layout}, auto_open=True, filename=("4DPlot.html"))

