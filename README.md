# KDD2018-FreshAir

学习

## Main2.py

根据运行时的时间，选择最近的能够从服务器获取完整数据的一天，获取那一天的数据，补全数据中空缺的单元格，复制一倍并按照提交格式输出到文件，作为最近48小时的预测数据。

数据补全规则：对每个监测站邻近线性插值；如果这个监测站一整天都没有数据，就随便使用另一个监测站的数据。
