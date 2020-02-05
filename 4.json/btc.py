# coding: utf-8

# ## 16.2 制作收盘价走势图：JSON 格式
# 在本节中，你将下载JSON格式的收盘价数据，并使用`json`模块来处理它们。
# Pygal提供了一个适合初学者使用的绘图工具，可以用它对收盘价数据进行可视化，以探索价格的特征。
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
import json
import certifi
# 读取网络json数据
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url, data=None, timeout=2000, cafile=certifi.where())
req = response.read()
with open('数据可视化/json/btc_close_2017_url.json', 'wb') as f:
    f.write(req)
# 加载json
file_urllib = json.load(req)
print(file_urllib)
