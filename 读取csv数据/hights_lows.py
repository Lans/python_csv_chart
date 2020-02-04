import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = '数据可视化/读取csv数据/sitka_weather_07-2014.csv'
filename2 = '数据可视化/读取csv数据/sitka_weather_2014.csv'
filename3 = '数据可视化/读取csv数据/death_valley_2014.csv'
# 读取csv文件
with open(filename3) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    for index, column_header in enumerate(header_row):
        # print(index, column_header)
        pass
    # 16.1.3 读取最高气温
    hights, dates, lows = [], [], []
    for row in reader:
        # 判断数字字符不为空,也可以try except
        # if len(row[1]) > 0:
        #     hight = int(row[1])
        #     hights.append(hight)
        try:
            hight = int(row[1])
            low = int(row[3])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print("data miss")
        else:
            hights.append(hight)
            lows.append(low)
            # 获取日期
            dates.append(current_date)
    # print(hights)

# 16.1.4 绘制气温图表
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, hights, c='red')
plt.plot(dates, lows, c='blue')
# 16.1.9 给图表区域添加颜色
plt.fill_between(dates, hights, lows, facecolor='blue', alpha=0.1)
# 设置图标标题 ，给坐标加上标签
plt.title("Daily high temp", fontsize=24)
plt.xlabel("", fontsize=14)
# 修改日期显示方式
fig.autofmt_xdate()
plt.ylabel("Temp(F)", fontsize=14)
# 设置想x，y轴刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
# 16.1.5 DateTime
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)
# 16.1.8 再绘制一个数据系列
