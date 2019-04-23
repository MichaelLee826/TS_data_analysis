import os
import csv
import datetime

# 输出文件-列车
out_file_train = open("F:\\上海地铁原始数据\\train.csv", 'a', newline='')
csv_write_train = csv.writer(out_file_train, dialect='excel')
headers_train = ['Train', 'Time', 'AvgNumber']
csv_write_train.writerow(headers_train)

# 输出文件-车站
out_file_station = open("F:\\上海地铁原始数据\\station.csv", 'a', newline='')
csv_write_station = csv.writer(out_file_station, dialect='excel')
headers_station = ['Station', 'Time', 'AvgNumber']
csv_write_station.writerow(headers_station)

# 基准日期： 2019-01-01
origin_date = datetime.datetime(2019, 1, 1, 0, 0, 0, 0)

# 列车
dict_train = {}
list_train = ['1701', '1702', '1703', '1704', '1705', '1706', '1707', '1708', '1709', '1710', '1711', '1712', '1713',
              '1714', '1715', '1716', '1717', '1718', '1719', '1720', '1721', '1722']
for i in range(len(list_train)):
    dict_train.fromkeys(list_train[i])
    dict_train[list_train[i]] = [[] for j in range(90)]

# 车站
dict_station = {}
station_map = {"3": "东方绿洲站下行站台", "4": "东方绿洲站上行站台", "8": "朱家角站下行站台", "9": "朱家角站上行站台",
               "12": "淀山湖大道站下行站台", "13": "淀山湖大道站上行站台", "20": "赵巷站下行站台", "22": "徐泾北城站下行站台",
               "23": "徐泾北城站上行站台", "26": "诸光路站上行站台", "29": "虹桥火车站下行站台", "32": "虹桥火车站上行站台",
               "33": "漕盈路站下行站台", "34": "青浦新城站下行站台", "35": "汇金路站下行站台", "36": "嘉松中路站下行站台",
               "37": "徐盈路站下行站台", "38": "蟠龙路站下行站台", "39": "诸光路站下行站台", "40": "漕盈路站上行站台",
               "41": "青浦新城站上行站台", "42": "汇金路站上行站台", "43": "赵巷站上行站台", "44": "嘉松中路站上行站台",
               "45": "徐盈路站上行站台", "46": "蟠龙路站上行站台"}
list_station = list(station_map.values())
for ii in range(len(list_station)):
    dict_station.fromkeys(list_station[ii])
    dict_station[list_station[ii]] = [[] for jj in range(90)]

# 累加
base_path = "F:\\上海地铁原始数据\\站台统计数据"
file_list = os.listdir(base_path)
for i in range(len(file_list)):
    path = os.path.join(base_path, file_list[i])
    print("processing:" + path)
    csv_file = open(path, 'r', encoding='utf-8')
    for one_line in csv_file:
        items = one_line.strip().split(',')
        if items[0] == "metro":
            continue
        date = datetime.datetime.strptime(items[1], "%Y-%m-%d %H:%M:%S.%f")
        index = (date - origin_date).days

        # 列车-累加
        train_no = items[0]
        dict_train[train_no][index].append(items[57])

        # 车站-累加
        station_no = items[38]
        # 判断是否是正线运行
        if station_no in station_map.keys():
            dict_station[station_map[station_no]][index].append(items[57])
        else:
            continue
        # print(item[38])     # 当前站台号
        # print(item[57])     # 基准值

# 计算并输出-列车
total = 0.0
average = 0.0
for j in range(len(list_train)):
    day_list = dict_train[list_train[j]]
    for k in range(90):
        total = 0.0
        average = 0.0
        load_list = day_list[k]
        length = len(load_list)
        # print(length)
        # print(load_list)
        if length == 0:
            continue
        for m in range(length):
            total += float(load_list[m])
        average = round((total / length), 3)
        delta = datetime.timedelta(days=k)
        date = (origin_date + delta).strftime("%Y-%m-%d")
        csv_write_train.writerow((list_train[j] + "," + date + "," + str(average)).strip().split(','))
        # print(list_train[j] + "---" + date + "---" + str(average))
out_file_train.close()

# 计算并输出-车站
total = 0.0
average = 0.0
for j in range(len(list_station)):
    day_list = dict_station[list_station[j]]
    for k in range(90):
        total = 0.0
        average = 0.0
        load_list = day_list[k]
        length = len(load_list)
        # print(length)
        # print(load_list)
        if length == 0:
            continue
        for m in range(length):
            total += float(load_list[m])
        average = round((total / length), 3)
        delta = datetime.timedelta(days=k)
        date = (origin_date + delta).strftime("%Y-%m-%d")
        csv_write_station.writerow((list_station[j] + "," + date + "," + str(average)).strip().split(','))
out_file_station.close()
