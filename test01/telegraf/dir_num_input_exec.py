import glob
import sys
import time

# 获取给定目录下的文件数

# 定义输出的模板字符串
template = "PathFileNum,name=test num={num} {timestamp}"
# 测试打印值
# print(template.format(num=1,timestamp=2))

# 获取传入的第一个参数
path = sys.argv[1]
# 使用glob进行文件匹配，得到匹配的文件数量
path_file_num = glob.glob(path).__len__()
# 套用模板
data = template.format(num=path_file_num)
print(data)
sys.exit(0)
# python dir_num_input_exec.py ./
