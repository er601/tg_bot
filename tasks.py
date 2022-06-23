# 1. Есть три листа:
#     list1 = [ 1, 2, 3, 4 ] ,
#     list2 = [ 8, 12, 45, 67, 89, 45 ] ,
#     list3 = [ 78, 90, 65 ]
#
# 2. Написать логику для добавления дополнительных элементов для листа по очереди индекса
#
# 3. Вывод : list1 = [ 1, 2, 3, 4, 1, 2, 3, 4 ],
# list2 = [ 8, 12, 45, 67, 89, 45, 8, 12, 45, 67, 89,45 ],
# list3 = [ 78, 90, 65, 78, 90, 65 ]

list1 = [1, 2, 3, 4]
list2 = [8, 12, 45, 67, 89, 45]
list3 = [78, 90, 65]

list1_copy = list1.copy()
list1.extend(list1_copy)
print('list1 =', list1)

list2_copy = list2.copy()
list2.extend(list2_copy)
print('list2 =', list2)

list3_copy = list3.copy()
list3.extend(list3_copy)
print('list3 =', list3)


# ---Задача---------

class_points = [2, 4, 100, 70, 40, 66]
your_points = 66


def better_than_average(class_points, your_points):
    print(sum(class_points) / len(class_points))
    return False if sum(class_points) / len(class_points) > your_points else True


print(better_than_average(class_points, your_points))

# -------Задача--------


def seyshely_vacation(d):
    return (d * 40) if d <= 3 else (d * 40) - 20 if 3 < d < 7 else (d * 40) - 50


print(seyshely_vacation(2))
print(seyshely_vacation(4))
print(seyshely_vacation(8))


# --------Задача-----


def converter(usd):
    return round(usd * 6.75, 2)


print(converter(15))
print(converter(465))
