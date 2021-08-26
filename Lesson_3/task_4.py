#Сложный вариант
def my_func(x, y):
    if (int(x) > 0) and (int(y) < 0) and (str(abs(int(x)*int(y))).isdigit()) == True:
        i = 1
        result = 1
        while i <= abs(y):
            result = result * x
            i = i + 1
        result = 1 / result
        return result
    else:
        return print("Входные данные не соответствуют условию задачи!")


print(my_func(int(input("Введите действительно положительное число: ")), int(input("Введите целое отрицательное число: "))))


#Простой вариант

def my_func2(x, y):
    if (int(x) > 0) and (int(y) < 0) and (str(abs(int(x)*int(y))).isdigit()) == True:
        result2 = x ** y
        return result2
    else:
        return print("Входные данные не соответствуют условию задачи!")


print(my_func2(int(input("Введите действительно положительное число: ")), int(input("Введите целое отрицательное число: "))))
