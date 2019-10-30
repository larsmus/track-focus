from plotly import graph_objs as go
import pandas as pd
import numpy as np
import math
import glob, os

usernames = [file[file.find("_")+1:file.find(".csv")] for file in glob.glob("*.csv")]
data = [pd.read_csv(file) for file in glob.glob("*.csv")]

dates = [[timestamp[:timestamp.find(" at")] for timestamp in d["Start date"][1:]] for d in data]
unique = [np.unique(d, return_counts=True) for d in dates]

plotly.offline.plot({
    "data": [go.Scatter(x=u[0], y=u[1], name='Lars',
                         line=dict(color='firebrick', width=i))
             for i, u in enumerate(unique)],
    "layout": go.Layout(title="Be Focused")
}, auto_open=False, filename="focused_plot.html")