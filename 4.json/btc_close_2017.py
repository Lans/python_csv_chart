import requests
import json
import pygal
# requests 发https 请求时，需要忽略证书的验证
# requests.packages.urllib3.disable_warnings()
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# req = requests.get(json_url, timeout=2000, verify=False)
# # 存储数据为json文件
# with open('数据可视化/json/btc_close_requsets_2017.json', 'w') as f:
#     f.write(req.text)
# # 转成json
# file_requset = req.json()
# print(file_requset)
files_json = open("数据可视化/json/btc_close_requsets_2017.json")
file_requset = json.load(files_json)
# 设置绘图变量
dates, months, weeks, weekdays, closes = [], [], [], [], []

# 16.2.2 读取相关数据
for btc_dict in file_requset:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    # float 去除小数点再转为int
    close = int(float(btc_dict['close']))
    closes.append(close)
    # print("{} is month {} week {}, {}, the close price is {} RMB".format(
    #     date, month, week, weekday, close))

# 16.2.4 绘制折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价(¥)'
line_chart.x_labels = dates
N = 20
# x轴背个20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', closes)
line_chart.render_to_file('数据可视化/json/收盘价折线图.svg')
# 16.2.5 结束
