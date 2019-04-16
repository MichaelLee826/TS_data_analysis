import os
import csv


def get_mode(file_path):
    values = read_csv(file_path)
    mode = '-1'
    if len(values) == 0:
        mode = handle_exception(file_path)
    else:
        dict_map = get_dict(values)
        numbers = dict_map.values()
        nums = []
        for n in numbers:
            nums.append(n)
        increase = bubble_sort(nums)
        index = len(increase) - 1
        mode = list(dict_map.keys())[list(dict_map.values()).index(increase[index])]
    return mode


def get_min(file_path):
    values = read_csv(file_path)
    min = '-1'
    if len(values) == 0:
        min = handle_exception(file_path)
    else:
        dict_map = get_dict(values)
        keys = dict_map.keys()
        nums = []
        for key in keys:
            nums.append(key)
        increase = bubble_sort(nums)

        for index in range(len(increase)):
            if increase[index] == '0':
                continue
            else:
                min = increase[index]
                break
    return min


def read_csv(file_path):
    values = []
    csv_file = csv.reader(open(file_path, encoding='utf-8'))
    rows = [row for row in csv_file]
    for index in range(len(rows)):
        item = ','.join(rows[index]).split(',')
        time = ''.join(item[0])[11:13]
        if time == '00' or time == '01' or time == '02' or time == '03' or time == '04':
            values.append(item[2])
    return values


def handle_exception(file_path):
    result = ''
    csv_file = csv.reader(open(file_path, encoding='utf-8'))
    rows = [row for row in csv_file]
    for index in range(len(rows)):
        item = ','.join(rows[index]).split(',')
        if item[2] != '0':
            result = item[2]
            break
    return result


def get_dict(values):
    dict_map = {}
    for index in range(len(values)):
        key = values[index]
        if key in dict_map.keys():
            dict_map[key] = dict_map[key] + 1
        else:
            dict_map[key] = 1
    return dict_map


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def write_csv(out_path, write_lines):
    out = open(out_path, 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    headers = ['Min', 'Mode']
    csv_write.writerow(headers)
    for content in write_lines:
        write_lines = content.split(',')
        csv_write.writerow(write_lines)


if __name__ == '__main__':
    # file = "F:\\上海地铁原始数据\\1701\\M1车架1载荷_ZT33\\2019-01\\1701_2019-01-01.csv"
    # print(file)
    # min = get_min(file)
    # mode = get_mode(file)
    # print(min)
    # print(mode)

    base_path = "F:\\上海地铁原始数据\\1701"
    file_paths = ['M1车架1载荷_ZT33', 'M1车架2载荷_ZT34', 'M2车架1载荷_ZT35', 'M2车架2载荷_ZT36',
                  'M3车架1载荷_ZT37', 'M3车架2载荷_ZT38', 'M4车架1载荷_ZT39', 'M4车架2载荷_ZT40',
                  'Tc1车架1载荷_ZT31', 'Tc1车架2载荷_ZT32', 'Tc2车架1载荷_ZT41', 'Tc2车架2载荷_ZT42']

    for i in range(len(file_paths)):
        file_path = base_path + "\\" + file_paths[i] + '\\2019-01'
        file_list = os.listdir(file_path)
        write_lines = []
        for j in range(len(file_list)):
            path = os.path.join(file_path, file_list[j])
            min = get_min(path)
            mode = get_mode(path)
            # print(path + "-->非0最小值：" + min)
            # print(path + "-->众数：" + mode)
            write_lines.append(str(min) + "," + str(mode))
        write_csv(base_path + "\\" + file_paths[i] + ".csv", write_lines)
