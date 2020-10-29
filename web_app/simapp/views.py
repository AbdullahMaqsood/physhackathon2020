from django.shortcuts import render
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as off
import numpy as np


def start(request):
    return render(request, 'simapp/start.html', {'title': 'Home'})


def sim(request):

    x=np.linspace(0, 4, 1000)
    for i in x:
        y=np.sin(2 * np.pi * (x - 0.01 * i))
        sc = px.scatter(x, y, title="Hey, Im an example plot!")

    plot = off.plot(sc,output_type='div', include_plotlyjs=True)

    context = {'plot' : plot}

    return render(request, 'simapp/sim.html', context)

