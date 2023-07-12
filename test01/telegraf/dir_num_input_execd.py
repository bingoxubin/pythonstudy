import glob
import sys

# 定义输出的 模板字符串
template = "PathFileNum,name=test num={num}"
# 获取传入的第一个参数
path = sys.argv[1]
# 获取命令行参数，这个参数应当是一个路径
# 阻塞输入，代码执行后，在shell端输入随意值后才有输出
for _ in sys.stdin:
    # 使用glob进行文件匹配，得到匹配到文件数量
    path_file_num = glob.glob(path).__len__()
    # 构造数据
    data = template.format(num=path_file_num)
    # 标准输出数据
    print(data)
    # 一定要手动刷掉缓冲区
    # 除了使用sys库，你还可以在print()函数中将flush参数设为True
    sys.stdout.flush()