# coding: utf-8

import os
import numpy as np
import tensorflow as tf

class FreshAir:
    # 读取到的所有数据
    data = {
        'beijing_17_18_aq.csv': None,
        'beijing_17_18_meo.csv': None,
        'beijing_201802_201803_aq.csv': None,
        'beijing_201802_201803_me.csv': None,
        'Beijing_AirQuality_Stations_cn.csv': None,
        'Beijing_grid_weather_station.csv': None,
        'Beijing_historical_meo_grid.csv': None,
        'London_AirQuality_Stations.csv': None,
        'London_grid_weather_station.csv': None,
        'London_historical_aqi_forecast_stations_20180331.csv': None,
        'London_historical_aqi_other_stations_20180331.csv': None,
        'London_historical_meo_grid.csv': None,
        'sample_submission.csv': None,
    }

    # 依次读取每个输入文件中的数据，存到self.data中
    def readData(self):
        pass

    # 构建神经网络模型
    def buildNetwork(self):
        pass

    # 训练并导出到文件
    def train(self):
        pass

    # 执行模型
    def runModel(self):
        pass


if __name__ == '__main__':
    pass

