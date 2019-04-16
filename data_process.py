import os
import csv

global values


def process(rootPath):
    rootDir = rootPath
    list = os.listdir(rootDir)
    for i in range(0, len(list)):
        path = os.path.join(rootDir, list[i])
        read_csv(path)
    find_mode(rootPath)

def read_csv(filePath):
    global values
    csv_file = csv.reader(open(filePath, encoding='utf-8'))
    rows = [row for row in csv_file]
    for index in range(len(rows)):
        item = ','.join(rows[index]).split(',')
        time = ''.join(item[0])[11:13]
        if time == '00' or time == '01' or time == '02' or time == '03' or time == '04':
            values.append(item[2])
            #print(item[0] + "~" + item[1] + "~" + item[2])

def find_mode(rootPath):
    global values
    dict_map = {}
    for index in range(len(values)):
        key = values[index]
        if key in dict_map.keys():
            dict_map[key] = dict_map[key] + 1
        else:
            dict_map[key] = 1

    keys = dict_map.keys()
    nums = []
    for key in keys:
        nums.append(key)

    increase = bubbleSort(nums)
    writeList = []
    for index in range(len(increase)):
        print(increase[index] + ":" + str(dict_map[increase[index]]))
        writeList.append(increase[index] + "," + str(dict_map[increase[index]]))
    #write_csv(rootPath, writeList)


def bubbleSort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def write_csv(rootPath, writeList):

    out = open(rootPath + rootPath[17:len(rootPath) - 8] + "_python.csv", 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    headers = ['值', '次数']
    csv_write.writerow(headers)
    for content in writeList:
        writeLine = content.split(',')
        csv_write.writerow(writeLine)


if __name__ == '__main__':
    rootPaths = ["F:\\上海地铁原始数据\\1701\\M1车架1载荷_ZT33\\2019-01\\1701_2019-01-31.csv"]
    global values
    # for path in rootPaths:
    #     print("processing：" + path)
    #     values = []
    #     process(path)
    values = []
    read_csv(rootPaths[0])
    find_mode("F:\\上海地铁原始数据\\1701\\M1车架1载荷_ZT33\\2019-01")
    #print("finished")
