import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 忽略证书的验证
requests.packages.urllib3.disable_warnings()
url = 'https://api.github.com/search/repositories?q=python+language:python$sort=starts&order=desc'
url2 = 'https://api.github.com/search/repositories?q=topic:python+topic:python'
r = requests.get(url2)
print('code:', r.status_code)
# 获取返回的json
respose_json = r.json()
print(respose_json.keys())
# 17.1.5 处理数据字典
print('总共：', respose_json['total_count'])
# 查看有关仓库信息
reso_dicts = respose_json['items']
print(str.format('一共{}仓库', len(reso_dicts)))
# 查看第一个仓库
repo_dict = reso_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys ()):
#     print(key)
# 17.2 使用pygal可视化仓库
names, starts, plot_dicts = [], [], []
for repo_dict in reso_dicts:
    names.append(repo_dict['name'])
    starts.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

my_style = LS("#333366", base_style=LCS)
# 17.2.1 D=定制图标配置
chart_config = pygal.Config()
chart_config.x_label_rotation = 45
chart_config.show_legend = False
chart_config.title_font_size = 24
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000
chart = pygal.Bar(chart_config, style=my_style)
chart.title = '在Github上Start最多的Python项目'
chart.x_labels = names
# 17.2.2 创建提示工具
chart.add('', plot_dicts)
chart.render_to_file('数据可视化/5.使用api/start_python_github.svg')
# 17.3 结束
