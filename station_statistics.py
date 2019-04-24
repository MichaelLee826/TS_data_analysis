import os
import csv


def process():
    # 输出文件
    station_names = ["东方绿洲站下行站台", "东方绿洲站上行站台", "朱家角站下行站台", "朱家角站上行站台", "淀山湖大道站下行站台",
                     "淀山湖大道站上行站台", "赵巷站下行站台", "徐泾北城站下行站台", "徐泾北城站上行站台", "诸光路站上行站台",
                     "虹桥火车站下行站台", "虹桥火车站上行站台", "漕盈路站下行站台", "青浦新城站下行站台", "汇金路站下行站台",
                     "嘉松中路站下行站台", "徐盈路站下行站台", "蟠龙路站下行站台", "诸光路站下行站台", "漕盈路站上行站台",
                     "青浦新城站上行站台", "汇金路站上行站台", "赵巷站上行站台", "嘉松中路站上行站台", "徐盈路站上行站台",
                     "蟠龙路站上行站台"]
    station_files = [file for file in range(26)]
    station_writers = [writer for writer in range(26)]
    for i in range(len(station_names)):
        station_files[i] = open("F:\\上海地铁原始数据\\站台统计数据" + "\\" + station_names[i] + ".csv", 'a', newline='')
        station_writers[i] = csv.writer(station_files[i], dialect='excel')

    # 输入文件
    base_path = "F:\\上海地铁原始数据\\列车合并数据结果"
    file_list = os.listdir(base_path)

    for file in file_list:
        file_path = os.path.join(base_path, file)
        print(file_path)
        csv_file = open(file_path, 'r', encoding='utf-8')
        train_no = os.path.basename(file)[4:8]
        for one_line in csv_file:
            # 增加列车号
            item = (train_no + "," + one_line).strip().split(',')
            if train_no == "1701" or train_no == "1702":
                station_code = item[29]
            else:
                station_code = item[38]
            if station_code == "CY1" or station_code == "0":
                continue
            elif station_code == "3":
                station_writers[0].writerow(item)
            elif station_code == "4":
                station_writers[1].writerow(item)
            elif station_code == "8":
                station_writers[2].writerow(item)
            elif station_code == "9":
                station_writers[3].writerow(item)
            elif station_code == "12":
                station_writers[4].writerow(item)
            elif station_code == "13":
                station_writers[5].writerow(item)
            elif station_code == "20":
                station_writers[6].writerow(item)
            elif station_code == "22":
                station_writers[7].writerow(item)
            elif station_code == "23":
                station_writers[8].writerow(item)
            elif station_code == "26":
                station_writers[9].writerow(item)
            elif station_code == "29":
                station_writers[10].writerow(item)
            elif station_code == "32":
                station_writers[11].writerow(item)
            elif station_code == "33":
                station_writers[12].writerow(item)
            elif station_code == "34":
                station_writers[13].writerow(item)
            elif station_code == "35":
                station_writers[14].writerow(item)
            elif station_code == "36":
                station_writers[15].writerow(item)
            elif station_code == "37":
                station_writers[16].writerow(item)
            elif station_code == "38":
                station_writers[17].writerow(item)
            elif station_code == "39":
                station_writers[18].writerow(item)
            elif station_code == "40":
                station_writers[19].writerow(item)
            elif station_code == "41":
                station_writers[20].writerow(item)
            elif station_code == "42":
                station_writers[21].writerow(item)
            elif station_code == "43":
                station_writers[22].writerow(item)
            elif station_code == "44":
                station_writers[23].writerow(item)
            elif station_code == "45":
                station_writers[24].writerow(item)
            elif station_code == "46":
                station_writers[25].writerow(item)
            else:
                print(station_code)
    csv_file.close()


if __name__ == '__main__':
    process()
