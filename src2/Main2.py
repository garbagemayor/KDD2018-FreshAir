import datetime
import requests
import shutil

class PlanB:
    url_template = 'https://biendata.com/competition/%s/%s/2018-%02d-%02d-00/2018-%02d-%02d-23/2k0d1d8'
    file_name_template = '../data/2/%s_st_%s_%02d-%02d_request.csv'
    submission_name_template = '../data/2/st_%s_%02d-%02d_submission.csv'

    base = None
    city = None
    month = None
    day = None
    full_base = None
    url = None
    file_name = None
    submission_name = None
    stationList = None
    file_data = None

    def __init__(self, base, city, month, day):
        self.base = base
        self.city = city
        self.month = month
        self.day = day
        self.full_base = 'airquality' if base == 'aq' else 'meteorology'
        self.url = self.url_template % (self.full_base, city, month, day, month, day)
        self.file_name = self.file_name_template % (city, base, month, day)
        self.submission_name = self.submission_name_template % (base, month, day)

    def getDataFromUrl(self):
        print("正在从网络获取天气数据：%s" % (self.file_name))
        with open(self.file_name, 'w') as f:
            f.write(requests.get(self.url).text)

    def getStationList(self):
        if self.city == 'bj':
            st_file_name = '../data/Beijing_AirQuality_Stations_cn.csv'
        else:
            st_file_name = '../data/London_AirQuality_Stations.csv'
        self.stationList = []
        for line in open(st_file_name):
            elem = line.split(',')
            if elem[0] == 'stationId' or elem[0] == '':
                continue
            if self.city == 'ld' and elem[2] != 'TRUE':
                continue
            self.stationList.append(elem[0])

    def translateToSubmission(self):
        print("正在转换格式")
        # 把空气数据按观测站划分到各自的list里面，翻倍变成第0~47小时
        file_data = {}
        for line in open(self.file_name):
            elem = line.split(',')
            if len(elem) <= 7 or elem[0] == 'id':
                continue
            if elem[1] not in file_data:
                file_data[elem[1]] = [[None] * 3] * 48
            def getHour(utcStr):
                try:
                    return int(elem[2].split(' ')[1].split(':')[0])
                except Exception:
                    return None
            def toFloat(xStr):
                try:
                    x = float(xStr)
                    return x if x >= 0 else 0
                except Exception:
                    return None
            tmp_aq = [
                toFloat(elem[3]),
                toFloat(elem[4]),
                toFloat(elem[7]),
            ]
            file_data[elem[1]][getHour(elem[2])] = tmp_aq
            file_data[elem[1]][getHour(elem[2]) + 24] = tmp_aq
        # 然后填充中间缺损的数据
        for station in file_data:
            for i in range(3):
                en_hour = 0
                while en_hour < 24 and file_data[station][en_hour][i] == None:
                    en_hour += 1
                while en_hour < 24:
                    st_hour = en_hour
                    while st_hour < 48 and file_data[station][st_hour][i] != None:
                        st_hour += 1
                    if st_hour >= 48:
                        break
                    en_hour = st_hour
                    while en_hour < 48 and file_data[station][en_hour][i] == None:
                        en_hour += 1
                    if en_hour >= 48:
                        break
                    st_data = file_data[station][st_hour - 1][i]
                    en_data = file_data[station][en_hour][i]
                    for h in range(st_hour, en_hour):
                        tmp = (st_data * (en_hour - h) + en_data * (h - st_hour + 1)) / (en_hour - st_hour + 1)
                        file_data[station][h][i] = tmp
            # 然后补充边缘缺损数据
            for h in range(48):
                for i in range(3):
                    if file_data[station][h][i] == None:
                        if h < 24:
                            file_data[station][h][i] = file_data[station][h + 24][i]
                        else:
                            file_data[station][h][i] = file_data[station][h - 24][i]
        # 最后解决彻底缺损的数据
        for station in file_data:
            for h in range(48):
                for i in range(3):
                    if file_data[station][h][i] == None:
                        flag = False
                        for st in file_data:
                            if file_data[st][h][i] != None:
                                file_data[station][h][i] = file_data[st][h][i]
                                flag = True
                                break
                        if flag == True:
                            continue
                        for hh in range(h - 1, -1, -1):
                            if file_data[station][hh][i] != None:
                                file_data[station][h][i] = file_data[station][hh][i]
                                flag = True
                                break
                        if flag == True:
                            continue
                        file_data[station][h][i] = 0
        self.file_data = file_data

    def writeSubmission(self):
        print("正在输出到文件：%s" % (self.submission_name))
        if self.city == 'bj':
            fout = open(self.submission_name, 'w')
            fout.write("test_id,PM2.5,PM10,O3\n")
        else:
            fout = open(self.submission_name, "a")
        for station in self.file_data:
            if station not in self.stationList:
                continue;
            for hour in range(48):
                tmp = self.file_data[station][hour]
                if self.city == 'bj':
                    fout.write("%s#%d,%f,%f,%f\n" % (station, hour, tmp[0], tmp[1], tmp[2]))
                else:
                    fout.write("%s#%d,%f,%f,\n" % (station, hour, tmp[0], tmp[1]))
        fout.close()

    def run(self):
        self.getDataFromUrl()
        self.getStationList()
        self.translateToSubmission()
        self.writeSubmission()
        shutil.copy(self.submission_name, '../data/2/submission.csv')

if __name__ == '__main__':
    rt = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    pb_bj = PlanB('aq', 'bj', rt.month, rt.day)
    pb_bj.run()
    pb_ld = PlanB('aq', 'ld', rt.month, rt.day)
    pb_ld.run()