import sys

# 循环获取标准输入
for line in sys.stdin:
    # 给输入前面加点东西接着输出
    print("bingo"+line,end="",flush=True)