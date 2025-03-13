from dash import Dash, dcc, html, dash_table
import pycaret
from pycaret.classification import *
import pandas as pd
import numpy as np
import dash.dependencies
from dash.dependencies import Output, Input
import plotly.express as px
import pycaret.regression
from pycaret.regression import predict_model, load_model
from datetime import datetime, timedelta
import pickle
import plotly.graph_objs as go


external_stylesheets = ['http://localhost:5500/styles.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

# general information
df1 = pd.read_csv('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\clean_data\\cleaned_data.csv')
df1["timestamp"] = pd.to_datetime(df1["timestamp"], format="%Y-%m-%d %H:%M:%S")
df1.sort_values("timestamp", inplace=True)

# calendar
calendar_start_date = df1['timestamp'].iloc[0]
calendar_end_date = df1['timestamp'].iloc[-1]


# data pm2.5
df2 = pd.read_csv('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\trainpredict_pm25.csv')
df2["timestamp"] = pd.to_datetime(df2["timestamp"], format="%Y-%m-%d %H:%M:%S")
df2.sort_values("timestamp", inplace=True)

# data O3
df3 = pd.read_csv('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\trainpredict_humidity.csv')
df3["timestamp"] = pd.to_datetime(df3["timestamp"], format="%Y-%m-%d %H:%M:%S")
df3.sort_values("timestamp", inplace=True)


# layout for homepage
homepage_layout = html.Div(
    id='homepage-container',
    children=[
        html.H1('CAR PAYAKORN /ᐠ≽•ヮ•≼マ ', style={'textAlign': 'center'}),
        html.Img(
            src='/assets/carmeme.jpg',  # Dash โหลดไฟล์จาก assets/ อัตโนมัติ
        style={'display': 'block', 'margin': '0 auto', 'height': '200px'}),
        html.Br(),
        dcc.Link('🐈 PM2.5 FORECAST FOR NEXT 7 DAYS 🐈', href='/pm25-next7days', className='link-item'),
        html.Br(),
        dcc.Link('🐈 HUMIDITY FORECAST FOR NEXT 7 DAYS 🐈', href='/hum-next7days', className='link-item'),
        html.Br(),
        dcc.Link('🐈 OVERALL INFORMATION 🐈', href='/overall-info', className='link-item'),
        html.Br(),
        dcc.Link('🐈 PM2.5 🐈', href='/pm25-forecasting', className='link-item'),
        html.Br(),
        dcc.Link('🐈 HUMIDITY 🐈', href='hum-forecasting', className='link-item')
    ]
)


# PM2.5 for next 7 days
def pm25_chart_prediction(n_intervals):
    train_pm25 = pd.read_csv('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\trainpredict_pm25.csv')
    train_pm25['timestamp'] = pd.to_datetime(train_pm25['timestamp'])

    loaded_model_PM25 = load_model('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\pm_2_5')
    now = pd.Timestamp.now()
    startdate = now.date()
    enddate = startdate + pd.DateOffset(days=7)
    next25_week = pd.date_range(start=startdate, end=enddate, freq='D')

    next25_data = pd.DataFrame({'timestamp': next25_week})
    next25_data['pm_2_5'] = train_pm25['pm_2_5'].mean().round(2)
    next25_data['humidity'] = train_pm25['humidity'].mean().round(2)
    next25_data['temperature'] = train_pm25['temperature'].mean().round(2)

    predictions_PM25 = predict_model(loaded_model_PM25, data=next25_data)
    predictions_PM25 = predictions_PM25.rename(columns={'Label': 'prediction_label'})
    predictions_PM25['prediction_label'] = predictions_PM25['prediction_label'].round(2)
    
    return next25_week, predictions_PM25

# Call  function  predictions
next25_week, predictions_PM25 = pm25_chart_prediction(0)

# DataFrame for plotting
pm25_plot = pd.DataFrame({'timestamp': next25_week, 'prediction_label': predictions_PM25['prediction_label']})
pm25_plot["prediction_label"] = pm25_plot["prediction_label"].round(2)

# Plot predictions 

next7_pm25_layout = html.Div([
    dcc.Graph(
        id='pm25-predictions',
        figure={
            'data': [
                {'x': pm25_plot['timestamp'], 'y': pm25_plot['prediction_label'], 'type': 'line', 'name': 'PM2.5 Prediction'}
            ],
            'layout': {
                'title': 'PM2.5 Prediction for Next 7 Days',
                'xaxis': {'title': 'DATE'},
                'yaxis': {'title': 'PM2.5'}
            }
        }
    )
])

# humidity for next 7 days
def hum_chart_prediction(n_intervals):
    train_hum = pd.read_csv('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\trainpredict_humidity.csv')
    train_hum['timestamp'] = pd.to_datetime(train_hum['timestamp'])

    loaded_model_hum = load_model('D:\\7\\66-psu\\year2\\semester2\\ba ai\\termpro-predictPM25\\humidity')
    now = pd.Timestamp.now()
    startdate = now.date()
    enddate = startdate + pd.DateOffset(days=7)
    next3_week = pd.date_range(start=startdate, end=enddate, freq='D')

    next3_data = pd.DataFrame({'timestamp': next3_week})
    next3_data['pm_2_5'] = train_hum['pm_2_5'].mean().round(2)
    next3_data['humidity'] = train_hum['humidity'].mean().round(2)
    next3_data['temperature'] = train_hum['temperature'].mean().round(2)

    predictions_hum = predict_model(loaded_model_hum, data=next3_data)
    predictions_hum = predictions_hum.rename(columns={'Label': 'prediction_label'})
    predictions_hum['prediction_label'] = predictions_hum['prediction_label'].round(2)
    
    return next3_week, predictions_hum

# Call  function  predictions
next3_week, predictions_hum = hum_chart_prediction(0)

# DataFrame for plotting
hum_plot = pd.DataFrame({'timestamp': next3_week, 'prediction_label': predictions_hum['prediction_label']})
hum_plot["prediction_label"] = hum_plot["prediction_label"].round(2)

# Plot predictions 

next7_hum_layout = html.Div([
    dcc.Graph(
        id='hum-predictions',
        figure={
            'data': [
                {'x': hum_plot['timestamp'], 'y': hum_plot['prediction_label'], 'type': 'line', 'name': 'Humidity Prediction'}
            ],
            'layout': {
                'title': 'HUMIDITY Prediction for Next 7 Days',
                'xaxis': {'title': 'DATE'},
                'yaxis': {'title': 'HUMIDITY'}
            }
        }
    )
])

# overall info page
overall_info_layout = html.Div([
    html.H2(children='OVERALL INFORMATION', style={'textAlign': 'center'}),
    dash_table.DataTable(
        id='datatable',
        columns=[{'name': i, 'id': i} for i in df1.columns],
        data=df1.to_dict('records'),
        page_size=10,
        style_table={
            'maxWidth': '600px',
            'margin': '50px auto',
            'padding': '20px',
            'border': '2px solid #d4ccc4',
            'borderRadius': '10px',
            'boxShadow': '0px 0px 10px rgba(0, 0, 0, 0.1)',
            'backgroundColor': '#fff',
        },
        style_header={
            'backgroundColor': '#9b9484',
            'color': '#fff',
        },
        style_cell={
            'padding': '10px',
        },
        style_data={
            'backgroundColor': '#f9f9f9',
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': '#e9e9e9'
            }
        ]
    )
])

# PM2.5 forecast
pm25_layout = html.Div([
    html.H2(children='PM2.5 DATA', style={'textAlign': 'center'}),
    dcc.DatePickerRange(
        id='pm25-date-range-picker',
        start_date_placeholder_text="Start Period",
        end_date_placeholder_text="End Period",
        calendar_orientation='vertical',
        start_date=calendar_start_date,
        end_date=calendar_end_date
    ),
    dcc.Graph(id='pm25-graph-content')
])
# Callback update PM2.5 graph
@app.callback(
    Output('pm25-graph-content', 'figure'),
    [Input('pm25-date-range-picker', 'start_date'),
     Input('pm25-date-range-picker', 'end_date')]
)
def pm25_update_graph(start_date, end_date):
    if start_date is None or end_date is None:
        return px.line()  # Empty plot
    dff2 = df2[(df2['timestamp'] >= start_date) & (df2['timestamp'] <= end_date)]
    return px.line(dff2, x='timestamp', y='pm_2_5')

# humidity forecast 
hum_layout = html.Div([
    html.H2(children='HUMIDITY DATA', style={'textAlign': 'center'}),
    dcc.DatePickerRange(
        id='hum-date-range-picker',
        start_date_placeholder_text="Start Period",
        end_date_placeholder_text="End Period",
        calendar_orientation='vertical',
        start_date=calendar_start_date,
        end_date=calendar_end_date
    ),
    dcc.Graph(id='hum-graph-content')
])

# Callback update humidity graph
@app.callback(
    Output('hum-graph-content', 'figure'),
    [Input('hum-date-range-picker', 'start_date'),
     Input('hum-date-range-picker', 'end_date')]
)
def hum_update_graph(start_date, end_date):
    if start_date is None or end_date is None:
        return px.line()  # Empty plot
    dff3 = df3[(df3['timestamp'] >= start_date) & (df3['timestamp'] <= end_date)]
    return px.line(dff3, x='timestamp', y='humidity')



@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/pm25-next7days':
        return next7_pm25_layout
    elif pathname == '/hum-next7days':
        return next7_hum_layout
    elif pathname == '/overall-info':
        return overall_info_layout
    elif pathname == '/pm25-forecasting':
        return pm25_layout
    elif pathname == '/hum-forecasting':
        return hum_layout
    else:
        return homepage_layout

# layout links page 
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])








app.config.suppress_callback_exceptions = True

# Run the app
if __name__ == '__main__':
    app.run(debug=True)