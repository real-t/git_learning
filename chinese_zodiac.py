# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

# print(chinese_zodiac[0:4])
# print(chinese_zodiac[-1])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])

print('狗' in chinese_zodiac)

print(chinese_zodiac + 'abcd')

print(chinese_zodiac * 3)

# 练习三列表的基本操作
# 定义一个含有5个数字的列表
# 为列表增加一个元素100
# 使用remove()删除一个元素后观察列表的变化
# 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

list1 = [1, 2, 3, 4, 5]
list1.append(100)
print(list1)
list1.remove(2)
print(list1)
print(list1[0:3])
print(list1[-1])

# 练习四元组的基本操作
# 定义一个任意元组，对元组使用append()查看错误信息
# 访问元组中的倒数第二个元素
# 定义一个新的元组，和1的元组连接成一个新的元组
# 计算元组元素个数
tuple1 = ("aa", "bb", "cc")
# tuple1.append("dd")
print(tuple1[-2])
tuple2 = ("dd", "ee", "ff")
tuple3 = tuple1 + tuple2
print(tuple3)
print(len(tuple3))
print(tuple3.__len__())
