import matplotlib.pyplot as plt

plt.figure()
plt.plot([1, 0, 9], [4, 5, 6])
plt.show()

#展现上海一周的天气,比如从星期一到星期日的天气温度如下
#1.创建画布(容器层)
plt.figure()
#2.绘制折线图(图像层)
plt.plot([1, 2, 3, 4, 5, 6 ,7], [17, 17, 18, 15, 11, 11, 13])
#3.显示图像
plt.show()
#可以看到这样显示效果并不好，我们可以加入更多的功能：