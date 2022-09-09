"""
Usuage : 

python3 main.py --method 'lstm_way'

"""
import argparse
import math
import os
import random
import sys
import time
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import matplotlib.pyplot as plt
from prophet import Prophet
import plotly.express as px
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
from ml.utils.general import (LOGGER, check_requirements, check_version, colorstr, increment_path, init_seeds)
from datetime import datetime
from sklearn.metrics import mean_absolute_error

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative

def read_data(file_name):
    df = pd.read_excel(file_name)
    return df

def Prophet_way():

    # Prophet model
    df = read_data('ml/Tomato_price_data.xlsx')
    df_pm = df.rename(columns={'date_time':'ds', 'avg':'y'})
    df_pm = df_pm.drop(['product_name','min','max'], axis=1)
    df_pm['ds']= pd.to_datetime(df_pm['ds'])
    
    model = Prophet()
    model.fit(df_pm)

    # define the period for which we want a prediction
    future = list()
    for i in range(9,15):
        date = '2022-09-%02d' % i
        future.append([date])
    future = pd.DataFrame(future)
    future.columns = ['ds']
    future['ds']= pd.to_datetime(future['ds'])

    #print('Doing prediction for next few Days')
    # use the model to make a forecast
    forecast = model.predict(future)

    # summarize the forecast
    #print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].head())

    # plot forecast
    # model.plot(forecast)
    # plt.draw()
    # plt.show()

    # # Intercative plot
    # fig = px.line(forecast, x="ds", y="yhat", title='Price for next 5 days')
    # fig.show()


    ## Prediction for next few hours
    # create test dataset, remove last
    train = df_pm.drop(df_pm.index[-11:])
    #print(train)

    # define the model
    model = Prophet()
    # fit the model
    model.fit(train)

    # define the period for which we want a prediction
    future = list()
    for i in range(13, 24):
        date = '2022-09-08 %2d:00:00' % i
        future.append([date])
    future = pd.DataFrame(future)
    future.columns = ['ds']
    future['ds'] = pd.to_datetime(future['ds'])

    # use the model to make a forecast
    forecast = model.predict(future)


    # calculate MAE between expected and predicted values for last 12 hrs of 2022-09-08
    y_true = df_pm['y'][-11:].values
    # #print('y_true:',y_true)

    y_pred = forecast['yhat'].values
    # #print('y_pred:',y_pred)
    #print('Doing prediction for next few hours')

    # plot forecast
    # model.plot(forecast)
    # plt.draw()
    # plt.show()
    #print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    mae = mean_absolute_error(y_true, y_pred)
    #print('MAE: %.3f' % mae)

    # # plot expected vs actual
    # plt.plot(y_true, label='Actual')
    # plt.plot(y_pred, label='Predicted')
    # plt.legend()
    # plt.draw()
    # plt.show()

# ************************************************************************************************
# LSTM Model
def lstm_way():
    df = read_data('ml/Tomato_price_data.xlsx')
    #print(df.head)
    df['date_time'] = pd.to_datetime(df['date_time'])
    df = df.iloc[:,1].values
    df = df.reshape(-1,1)
    df = df.astype("float32")
    # scaling 
    scaler = MinMaxScaler(feature_range=(0, 1))
    df = scaler.fit_transform(df)

    train_size = int(len(df) * 0.75)
    test_size = len(df) - train_size
    train = df[0:train_size,:]
    test = df[train_size:len(df),:]
    #print("train size: {}, test size: {} ".format(len(train), len(test)))


    time_stamp = 1

    dataX = []
    dataY = []

    for i in range(len(train)-time_stamp-1):
        a = train[i:(i+time_stamp), 0]
        dataX.append(a)
        dataY.append(train[i + time_stamp, 0])
        
    trainX = np.array(dataX)
    trainY = np.array(dataY)  


    dataX = []
    dataY = []
    for i in range(len(test)-time_stamp-1):
        a = test[i:(i+time_stamp), 0]
        dataX.append(a)
        dataY.append(test[i + time_stamp, 0])
    testX = np.array(dataX)
    testY = np.array(dataY)  


    trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

    model = Sequential()

    model.add(LSTM(units=8,input_shape = (1, time_stamp)))
    model.add(Dense(1))

    model.compile(optimizer='adam',loss='mean_squared_error')

    model.fit(trainX, trainY, epochs=10, batch_size=1,verbose=2)


    trainPredict = model.predict(trainX)
    testPredict = model.predict(testX)

    # invert predictions
    trainPredict = scaler.inverse_transform(trainPredict)
    trainY = scaler.inverse_transform([trainY])
    testPredict = scaler.inverse_transform(testPredict)
    testY = scaler.inverse_transform([testY])

    # calculate root mean squared error
    trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
    #print('Train Score: %.2f RMSE' % (trainScore))
    testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
    #print('Test Score: %.2f RMSE' % (testScore))

    # shifting train
    trainPredictPlot = np.empty_like(df)
    trainPredictPlot[:, :] = np.nan
    trainPredictPlot[time_stamp:len(trainPredict)+time_stamp, :] = trainPredict

    # shifting test
    testPredictPlot = np.empty_like(df)
    testPredictPlot[:, :] = np.nan
    testPredictPlot[len(trainPredict)+(time_stamp*2)+1:len(df)-1, :] = testPredict

    # #print(trainPredictPlot)
    # plt.plot(scaler.inverse_transform(df))
    # plt.plot(trainPredictPlot)
    # plt.plot(testPredictPlot)
    # plt.draw()
    # plt.show()


def predict():

    results = Prophet_way()
    
    return results
# lstm_way()