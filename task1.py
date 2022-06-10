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
