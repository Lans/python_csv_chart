# coding=UTF-8
# python3
import matplotlib.pyplot as plt

# 折线图
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
# 设置图标标题 ，给坐标加上标签
plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares Value", fontsize=14)
# 设置想x，y轴刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
