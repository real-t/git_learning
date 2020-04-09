# 这是我的第一个Python程序

import time # 我导入了一个时间模块

print(time.time()) #在屏幕上打印出从1970年1月1日0：00到现在经过了多少秒

if 10-9 > 0:
    # 这行需要缩进，缩进用4个空格
    print('10大于9')

# 练习一变量的定义和使用
# 定义两个变量分别为美元和汇率
dollar = 100
exchange = 7.066
# 使用Python计算100美元兑换的人民币数量并用print()进行输出
print('{dol}美元兑换人民币数量为{yuan}'.format(dol=dollar, yuan=dollar * exchange))
