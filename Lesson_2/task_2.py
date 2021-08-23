list1 = input("Введите список через пробел: ").split(" ")
i = 0
while i < len(list1)-1:
    temp = list1[i+1]
    list1[i+1] = list1[i]
    list1[i] = temp
    i = i + 2
print("Поменяв местами четные и нечетные элементы списка получим",list1)
