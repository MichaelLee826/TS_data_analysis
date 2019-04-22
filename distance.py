from geopy.distance import geodesic
import xlrd
import csv


distance_file = open("F:\\上海地铁原始数据\\distance.csv", 'a', newline='')
csv_write = csv.writer(distance_file, dialect='excel')
headers = ['station', 'distance']
csv_write.writerow(headers)

file_path = "F:\\上海地铁原始数据\\17号线57个站点GPS数据.xls"
workbook = xlrd.open_workbook(file_path)
sheet = workbook.sheet_by_index(0)
rows = sheet.nrows
longitude = sheet.col_values(3)
latitude = sheet.col_values(4)
distance = [0 for i in range(rows - 1)]
for index in range(1, rows - 1):
    distance[index] = geodesic((latitude[index], longitude[index]), (latitude[index + 1], longitude[index + 1])).km
    distance[index] = round(distance[index], 3)
    result = [index, distance[index]]
    csv_write.writerow(result)
distance_file.close()
