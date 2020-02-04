import matplotlib.pyplot as plt

# 散点图
# plt.scatter(2, 4, s=200)
# x_value = [1, 2, 3, 4, 5]
# y_value = [1, 4, 9, 16, 25]
x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]
plt.scatter(x_value,
            y_value,
            c=y_value,
            cmap=plt.cm.Blues,
            edgecolor='none',
            s=40)
# 设置图标标题 ，给坐标加上标签
plt.title("Squares Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares Value", fontsize=14)
# 设置想x，y轴刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置取值范围
plt.axis([0, 1100, 0, 1100000])
# 保存图标图片到本地
# plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()


# 结束语15.3.1
