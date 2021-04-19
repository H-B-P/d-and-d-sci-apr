import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv("dset.csv")

print(len(df))
print(len(df[df["damage taken"]=="100%+"]))

df = df[df["damage taken"]!="100%+"]

def shear(st):
 return int(st.replace("%",""))

df["damage taken"]=df["damage taken"].apply(shear)

print(df)

for unique in df["encounter"].unique():
 sdf = df[df["encounter"]==unique]
 print(unique, len(sdf), sum(sdf["damage taken"]), sdf["damage taken"].mean())
 fig = go.Figure()
 fig.update_layout(xaxis={"range":[0,100]}, title=unique)
 fig.add_trace(go.Histogram(x=sdf["damage taken"],
                      xbins=dict(
                      start=0,
                      end=100,
                      size=1),#size=2
                      autobinx=False))
 #fig = px.histogram(sdf, x="damage taken", title=unique)#, nbins=100)
 #fig.update_layout(xaxis={"range":[0,100]})
 fig.show()
 



