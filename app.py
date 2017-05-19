#!/usr/bin/env python
# -*- coding: utf-8 -*-

import data
from flask import Flask, render_template
from altair import Chart, X, Y, Axis, Data, DataFormat
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


### Altair Data Routes

WIDTH = 600
HEIGHT = 300

@app.route("/data/bar")
def data_bar():
    chart = Chart(data=data.df_list, height=HEIGHT, width=WIDTH).mark_bar(color='lightgreen').encode(
        X('name', axis=Axis(title='Sample')),
        Y('data', axis=Axis(title='Value'))
    )
    return chart.to_json()


@app.route("/data/waterfall")
def data_waterfall():
    chart = Chart(data.df_water).mark_bar(color='lightgreen').encode(
        X('Name', axis=Axis(title='Sample')),
        Y('Value', axis=Axis(title='Value'))
    )
    return chart.to_json()


@app.route("/data/line")
def data_line():
    chart = Chart(data=data.df_list, height=HEIGHT, width=WIDTH).mark_line().encode(
        X('name', axis=Axis(title='Sample')),
        Y('data', axis=Axis(title='Value'))
    )
    return chart.to_json()


@app.route("/data/multiline")
def data_multiline():
    chart = Chart(data=data.df_stocks, height=HEIGHT, width=WIDTH).mark_line().encode(
        color='symbol:N',
        x='date:T',
        y='price:Q',
    )
    return chart.to_json()


@app.route("/data/stocks")
def stocks():
    chart = Chart(data=data.df_stocks, height=HEIGHT, width=WIDTH).mark_bar().encode(
        color='symbol:N',
        x='date:T',
        y='price:Q',
    )
    return chart.to_json()


@app.route("/data/scatter")
def scatter():
    chart = Chart(data.df_0, height=HEIGHT, width=WIDTH).mark_circle().encode(
        x='name:N',
        y='y2:Q'
    )
    return chart.to_json()


if __name__ == "__main__":
    app.run(debug=True)
