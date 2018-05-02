# coding: utf-8

import os
import numpy as np
import tensorflow as tf



class FreshAir:
    # 读取到的所有数据
    FILE_NAME = [
        'beijing_17_18_aq.csv',
        'beijing_17_18_meo.csv',
        'beijing_201802_201803_aq.csv',
        'beijing_201802_201803_me.csv',
        'Beijing_AirQuality_Stations_cn.csv',
        'Beijing_grid_weather_station.csv',
        'Beijing_historical_meo_grid.csv',
        'London_AirQuality_Stations.csv',
        'London_grid_weather_station.csv',
        'London_historical_aqi_forecast_stations_20180331.csv',
        'London_historical_aqi_other_stations_20180331.csv',
        'London_historical_meo_grid.csv',
        'sample_submission.csv',
    ]

    # 监测点的信息
    bj_st = {}
    ld_st = {}
    # 网格点的信息
    bj_gr = {}
    ld_gr = {}
    # 监测点的空气
    bj_st_aq = []



    # utc时间转换成整数，例如“2017-01-01 00:00:00”转换变成0
    def utcToInt(self, utcStr):
        try:
            ymd = utcStr.split(' ')[0]
            y = int(ymd.split('-')[0])
            m = int(ymd.split('-')[1])
            d = int(ymd.split('-')[2])
            hms = utcStr.split(' ')[1]
            h = int(hms.split(':')[0])
            dc = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            for i in range(1, len(dc)):
                dc[i] += dc[i - 1]
            return ((y - 2017) * 365 + dc[m - 1] + d - 1) * 24 + h
        except Exception:
            return None

    def strToFloat(self, xStr):
        try:
            return float(xStr)
        except Exception:
            return None

    # 依次读取每个输入文件中的数据，存到self.data中
    def readData(self):
        # 读北京监测点的信息
        id = 0
        for line in open('../data/Beijing_AirQuality_Stations_cn.csv'):
            elem = line.split(',')
            if elem[0] == 'stationId':
                continue
            self.bj_st[elem[0]] = {
                'id': id,
                'longitude': float(elem[1]),
                'latitude': float(elem[2]),
            }
            id += 1
        # print(self.bj_st)

        # 读伦敦监测点的信息
        id = 0
        for line in open('../data/London_AirQuality_Stations.csv'):
            elem = line.split(',')
            if elem[0] == '':
                continue
            self.ld_st[elem[0]] = {
                'id': id,
                'longitude': float(elem[5]),
                'latitude': float(elem[4]),
            }
            id += 1
        # print(self.ld_st)

        # 读北京网格点的信息
        for line in open('../data/Beijing_grid_weather_station.csv'):
            elem = line.split(',')
            id = int(elem[0][-3:])
            self.bj_gr[elem[0]] = {
                'id': id,
                'idX': id // 21,
                'idY': id % 21,
                'longitude': float(elem[2]),
                'latitude': float(elem[1]),
            }
        # print(self.bj_gr)

        # 读伦敦网格点的信息
        for line in open('../data/London_grid_weather_station.csv'):
            elem = line.split(',')
            id = int(elem[0][-3:])
            self.ld_gr[elem[0]] = {
                'id': id,
                'idX': id // 21,
                'idY': id % 21,
                'longitude': float(elem[2]),
                'latitude': float(elem[1]),
            }
        # print(self.ld_gr)

        # 读北京监测点的空气
        for line in open('../data/beijing_17_18_aq.csv'):
            elem = line.split(',')
            if elem[0] == 'stationId':
                continue
            self.bj_st_aq.append([
                self.bj_st[elem[0]]['id'],      # 监测点id
                self.utcToInt(elem[1]),         # 时间
                self.strToFloat(elem[2]),       # PM2.5
                self.strToFloat(elem[3]),       # PM10
                self.strToFloat(elem[6]),       # O3
                self.strToFloat(elem[4]),       # NO2
                self.strToFloat(elem[5]),       # CO
                self.strToFloat(elem[7]),       # SO2
            ])
        for line in open('../data/beijing_201802_201803_aq.csv'):
            elem = line.split(',')
            if elem[0] == 'stationId':
                continue
            self.bj_st_aq.append([
                self.bj_st[elem[0]]['id'],      # 监测点id
                self.utcToInt(elem[1]),         # 时间
                self.strToFloat(elem[2]),       # PM2.5
                self.strToFloat(elem[3]),       # PM10
                self.strToFloat(elem[6]),       # O3
                self.strToFloat(elem[4]),       # NO2
                self.strToFloat(elem[5]),       # CO
                self.strToFloat(elem[7]),       # SO2
            ])
        # print(self.bj_st_aq[:10])

        # 读北京网格点的空气
        for line in open('../data/Beijing_historical_meo_grid.csv'):






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
    fa = FreshAir()
    fa.readData()
