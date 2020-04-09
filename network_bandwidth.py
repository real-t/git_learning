# 网络带宽计算
# print(100/8)

bandwidth = 100 # 为变量赋值
ratio = 8

print(bandwidth/ratio)

# 练习一字符串
# 定义一个字符串Hello Python并使用print()输出
# 定义第二个字符串Let's go并使用print()输出
# 定义第三个字符串"TheZen of Python"--by Tim Peters并使用print()输出
string1 = 'Hello Python'
print(string1)
string2 = "Let's go"
print(string2)
string3 = '"TheZen of Python"--by Tim Peters'
print(string3)

# 练习二字符串基本操作
# 定义两个字符串分别为xyz、abc
# 对两个字符串进行连接
# 取出xyz字符串的第二个和第三个元素
# 对abc输出10次
# 判断a字符（串）在xyz和abc两个字符串中是否存在，并进行输出

string1 = "xyz"
string2 = "abc"
print(string1 + string2)
print(string1[1])
print(string1[2])
print(string2 * 10)
# if "a" in string1:
#     print(string1)
# if "a" in string2:
#     print("字符a在" + string2 + "字符串中存在")
print('a' in string1)
print('a' in string2)
