from die import Die
import pygal

# 一个六面骰子
die = Die()
results = []
for x in range(1000):
    result = die.roll()
    results.append(result)
# 分析结果,统计各点数出现的次数
frequencies = []
for value in range(1, die.num_sides + 1):
    frequencie = results.count(value)
    frequencies.append(frequencie)
# 对结果绘制表格
hist = pygal.Bar()
hist.title = "六面骰子的随机100测统计表"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "结果"
hist.y_title = "次数"

hist.add('D6', frequencies)
hist.render_to_file('diw_visual.svg')
