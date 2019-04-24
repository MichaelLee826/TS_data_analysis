import os
import csv


def process():
    # 输出文件
    station_dict = {"3": "东方绿洲站下行站台", "4": "东方绿洲站上行站台", "8": "朱家角站下行站台", "9": "朱家角站上行站台",
                    "12": "淀山湖大道站下行站台", "13": "淀山湖大道站上行站台", "20": "赵巷站下行站台", "22":"徐泾北城站下行站台",
                    "23": "徐泾北城站上行站台", "26": "诸光路站上行站台", "29": "虹桥火车站下行站台", "32": "虹桥火车站上行站台",
                    "33": "漕盈路站下行站台", "34": "青浦新城站下行站台", "35": "汇金路站下行站台", "36": "嘉松中路站下行站台",
                    "37": "徐盈路站下行站台", "38": "蟠龙路站下行站台", "39": "诸光路站下行站台", "40": "漕盈路站上行站台",
                    "41": "青浦新城站上行站台", "42": "汇金路站上行站台", "43": "赵巷站上行站台", "44": "嘉松中路站上行站台",
                    "45": "徐盈路站上行站台", "46": "蟠龙路站上行站台"}
    station_names = list(station_dict.values())
    station_files = [file for file in range(station_dict.__len__())]
    station_writers = [writer for writer in range(station_dict.__len__())]
    for i in range(station_dict.__len__()):
        station_files[i] = open("F:\\上海地铁原始数据\\站台统计数据_test" + "\\" + station_names[i] + ".csv", 'a', newline='')
        station_writers[i] = csv.writer(station_files[i], dialect='excel')

    # 输入文件
    base_path = "F:\\上海地铁原始数据\\列车合并数据结果"
    file_list = os.listdir(base_path)

    for file in file_list:
        file_path = os.path.join(base_path, file)
        print(file_path)
        csv_file = open(file_path, 'r', encoding='utf-8')
        train_no = os.path.basename(file)[4:8]
        flag = False
        line = ''
        index = -1
        for one_line in csv_file:
            # 增加列车号
            item = (train_no + "," + one_line).strip().split(',')
            station_code = item[38]
            if station_code == "CY1" or station_code == "0":
                if flag is False:
                    continue
                else:
                    station_writers[index].writerow(line)
                    flag = False
            elif station_code in station_dict.keys():
                flag = True
                line = item
                station_name = station_dict.get(station_code)
                index = station_names.index(station_name)
    csv_file.close()


if __name__ == '__main__':
    process()
