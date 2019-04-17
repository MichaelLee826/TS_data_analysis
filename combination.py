import os
import csv


def process():
    base_path = "F:\\上海地铁原始数据\\列车合并数据"
    result_path = "F:\\上海地铁原始数据\\列车合并数据结果"
    file_list = os.listdir(base_path)
    combination_name = ""
    for i in range(len(file_list)):
        file_name = os.path.basename(file_list[i])
        if combination_name == file_name[0:8]:
            print("合并第" + str(i) + "个")
            file_path = os.path.join(base_path, file_list[i])
            csv_file = open(file_path, 'r', encoding='utf-8')
            write_file(csv_file, result_file)
        else:
            print("创建第" + str(i) + "个")
            combination_name = file_name[0:8]
            result_file = open(result_path + "\\" + combination_name + ".csv", 'a', newline='')
            file_path = os.path.join(base_path, file_list[i])
            csv_file = open(file_path, 'r', encoding='utf-8')
            create_file(csv_file, result_file)


# 新建、合并
def create_file(from_file, to_file):
    csv_writer = csv.writer(to_file, dialect='excel')
    for one_line in from_file:
        csv_writer.writerow(one_line.strip().split(','))


# 合并
def write_file(from_file, to_file):
    csv_writer = csv.writer(to_file, dialect='excel')
    for one_line in from_file:
        # 合并时去掉首行
        if "time" in one_line:
            continue
        csv_writer.writerow(one_line.strip().split(','))


if __name__ == '__main__':
    process()
