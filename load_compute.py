import os
import csv

computation = [19.4, 17.3, 18.74, 18.44, 19.3, 19.14, 19.3, 19.3, 18.84, 18.9, 17.2, 19.4]
collect_mode = ['-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', ]
collect_min = ['-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', '-1', ]


def process():
    base_path = "F:\\上海地铁原始数据\\BigFiles"
    file_list = os.listdir(base_path)
    for i in range(len(file_list)):
        path = os.path.join(base_path, file_list[i])
        print("processing:" + path)
        csv_file = csv.reader(open(path, encoding='utf-8'))
        rows = [row for row in csv_file]

        out = open("F:\\上海地铁原始数据\\statistics.csv", 'a', newline='')
        csv_write = csv.writer(out, dialect='excel')
        headers = ['Time', '1-Mode', '1-Min', '2-Mode', '2-Min', '3-Mode', '3-Min', '4-Mode', '4-Min', '5-Mode',
                   '5-Min', '6-Mode', '6-Min']
        csv_write.writerow(headers)

        lists = [[] for count in range(12)]
        update = True
        for j in range(len(rows)):
            if j == 0:
                continue

            item = ','.join(rows[j]).split(',')
            time = ''.join(item[0])[11:13]
            if time == '00' or time == '01' or time == '02' or time == '03' or time == '04':
                lists[0].append(item[21])
                lists[1].append(item[22])
                lists[2].append(item[5])
                lists[3].append(item[6])
                lists[4].append(item[9])
                lists[5].append(item[10])
                lists[6].append(item[13])
                lists[7].append(item[14])
                lists[8].append(item[17])
                lists[9].append(item[18])
                lists[10].append(item[25])
                lists[11].append(item[26])
                update = True
            else:
                if update == True:
                    for k in range(len(lists)):
                        collect_min[k] = get_min(lists[k])
                        collect_mode[k] = get_mode(lists[k])
                update = False
                sensors = [item[21], item[22], item[5], item[6], item[9], item[10],
                           item[13], item[14], item[17], item[18], item[25], item[26]]
                write_lines = ['', '', '', '', '', '', '', '', '', '', '', '']
                for index in range(len(sensors)):
                    if index > 5:
                        break
                    a = int(sensors[2 * index])
                    b = int(sensors[2 * index + 1])
                    c = (a + b) * 0.01

                    num_collect_mode = (c - int(collect_mode[2 * index]) * 0.01 - int(
                        collect_mode[2 * index + 1]) * 0.01) / 0.06

                    num_collect_min = (c - int(collect_min[2 * index]) * 0.01 - int(
                        collect_min[2 * index + 1]) * 0.01) / 0.06

                    num_mode = str(round(num_collect_mode, 3))
                    num_min = str(round(num_collect_min, 3))

                    write_lines[2 * index] = num_mode
                    write_lines[2 * index + 1] = num_min

                    # write_lines[index] = str(round(num_collect_mode, 3)) + "---" + str(round(num_collect_min, 3))
                    # print(item[0] + ":" + str(round(num_collect_mode, 3)) + "---" + str(round(num_collect_min, 3)))

                string = item[0] + "," + write_lines[0] + "," + write_lines[1] + "," + write_lines[2] + "," + \
                         write_lines[3] + "," + write_lines[4] + "," + write_lines[5] + "," + write_lines[6] + "," + \
                         write_lines[7] + "," + write_lines[8] + "," + write_lines[9] + "," + write_lines[10] + "," + \
                         write_lines[11]
                temp = string.split(',')
                csv_write.writerow(temp)


def get_min(values):
    min = '-1'
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


def get_mode(values):
    mode = '-1'
    dict_map = get_dict(values)
    numbers = dict_map.values()
    nums = []
    for n in numbers:
        nums.append(n)
    increase = bubble_sort(nums)
    index = len(increase) - 1
    mode = list(dict_map.keys())[list(dict_map.values()).index(increase[index])]
    return mode


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


def compute(date_time, sensors):
    # print("-------------------------------------------")
    for index in range(len(sensors)):
        if index > 5:
            break
        a = int(sensors[2 * index])
        b = int(sensors[2 * index + 1])
        c = (a + b) * 0.01
        num_collect_mode = (c - int(collect_mode[2 * index]) * 0.01 - int(collect_mode[2 * index + 1]) * 0.01) / 0.06
        num_collect_min = (c - int(collect_min[2 * index]) * 0.01 - int(collect_min[2 * index + 1]) * 0.01) / 0.06
        # print(date_time + ":" + str(round(num_collect_mode, 3)) + "---" + str(round(num_collect_min, 3)))


if __name__ == '__main__':
    process()
