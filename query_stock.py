# -*- coding: utf-8 -*-
import sys
from plotly.tools import FigureFactory as FF
import plotly
from pandas_datareader import data
from datetime import datetime
from plotly.graph_objs import Scatter, Layout, Line
import numpy as np

# 算均線
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n



def query_stock(stock, start='2011.01.01', end='today'):
    stock+=".TW"
    st = datetime.date(datetime.strptime(start, '%Y.%m.%d'))

    if end == 'today':
        en = datetime.date(datetime.today())
    else:
        en = datetime.date(datetime.strptime(end, '%Y.%m.%d'))
    df = data.get_data_yahoo(stock, st, en)
    fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)
    SMA20=moving_average(df.Close.values, 20)
    add_line = Scatter(
        x=df.index[-len(SMA20):],
        y=SMA20,
        name= '20SMA',
        line=Line(color='rgb(200, 200, 250)')
        )
    fig['data'].extend([add_line])
    plotly.offline.plot(fig, validate=False)

if len(sys.argv) < 2:
    print 'no argument'
    sys.exit()
elif len(sys.argv) == 2:
    query_stock(sys.argv[1])
elif len(sys.argv) == 3:
    query_stock(sys.argv[1],sys.argv[2])
elif len(sys.argv) == 4:
    query_stock(sys.argv[1],sys.argv[2],sys.argv[3])
