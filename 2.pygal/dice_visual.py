from die import Die
import pygal

die = Die()
die2 = Die()
results = []
for x in range(1000):
    result = die.roll() + die2.roll()
    results.append(result)
# 分析结果,统计各点数出现的次数
frequencies = []
for value in range(2, die.num_sides + die2.num_sides + 1):
    frequencie = results.count(value)
    frequencies.append(frequencie)
# 对结果绘制表格
hist = pygal.Bar()
hist.title = "2个六面骰子的随机100测统计表"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "结果"
hist.y_title = "次数"

hist.add('D6+D6', frequencies)
hist.render_to_file('数据可视化/pygal/diw_visual2.svg')
