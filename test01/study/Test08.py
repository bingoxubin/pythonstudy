# matplotlib
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import random

# 绘制折线 x,y
plt.plot([1, 0, 9], [4, 5, 6])
plt.show()

# 折线图
x = range(1, 8)
y = [17, 17, 18, 15, 11, 11, 13]
# 颜色、透明度、线的样式、线的宽度、标记实心点，标记点大小,标记圈外的颜色,外圈宽度
plt.plot(x, y, color='red', alpha=0.5, linestyle='--', linewidth=3, marker='o', markersize=10, markeredgecolor='green',
         markeredgewidth=5)
plt.show()

# 图片保存
x = range(2, 26, 2)
y = [random.randint(15, 30) for i in x]
# 设置图片的大小,dpi分辨率
plt.figure(figsize=(20, 8), dpi=80)
# 绘制
plt.plot(x, y)
# 保存，图片的格式也可以保存为svg这种矢量图格式，这种矢量图放在网页中放大后不会有锯齿
plt.savefig('./source/t1.png')
# 展示,注意show的方法一定要在savafig的下面，并且plt.show()会释放figure资源，如果再显示图像之后保存图片将只能保存空图片
plt.show()

# 绘制x轴和y轴的刻度
x = range(2, 26, 2)
y = [random.randint(15, 30) for i in x]
# 设置图片的大小,dpi分辨率
plt.figure(figsize=(20, 8), dpi=80)
# 设置x轴刻度
# plt.xticks(x)
x_value = range(1, 25)
x_tick_lable = ["{}:00".format(i) for i in x_value]
# 两个参数分别是刻度、和刻度的值、倾斜45度
plt.xticks(x_value, x_tick_lable, rotation=45)

# 设置y轴刻度
y_value = range(min(y), max(y) + 1)
y_tick_lavel = ["{}°C".format(i) for i in y_value]
plt.yticks(y_value, y_tick_lavel)
# 绘制
plt.plot(x, y)
plt.show()

# 设置中文
x = range(0, 120)
y = [random.randint(10, 30) for i in range(120)]
# 设置图片的大小,dpi分辨率
plt.figure(figsize=(20, 8), dpi=80)
# 绘制
plt.plot(x, y)
# 展示,注意show的方法一定要在savafig的下面，并且plt.show()会释放figure资源，如果再显示图像之后保存图片将只能保存空图片
from matplotlib import font_manager

# 加载系统字体
my_font = font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc", size=18)
# 设置标题
plt.title("图片", fontproperties=my_font)
# x轴标题
plt.xlabel('时间', fontproperties=my_font)
# y轴标题
plt.ylabel('次数', fontproperties=my_font)
plt.show()

# 一图多线
y1 = [1, 0, 1, 1, 2, 4, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 4, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]

x = range(11, 31)
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y1, color='red', label='自己')
plt.plot(x, y2, color='blue', label='同事')

# 设置到x轴
xtick_labels = ['{}岁'.format(i) for i in x]
my_font = font_manager.FontProperties(fname="C:\\WINDOWS\\Fonts\\simsun.ttc", size=18)

plt.xticks(x, xtick_labels, fontproperties=my_font, rotation=45)
# 绘制网格
plt.grid(alpha=0.4)
# 添加图例
plt.legend(prop=my_font, loc='upper right')
plt.show()

# 汇总 图例：plt.legend(prop)  标题：plt.title   绘制图片:plt.plot  绘制网格：plt.grid  x轴：xticks   y轴：yticks

# 散点图  plt.scatter()
# 条形图  plt.bar()[纵向]  plt.barh()[横向]
# 直方图  plt.hist()
# 饼图 plt.pie
