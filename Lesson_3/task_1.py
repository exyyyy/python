def my_division(var_1 = float(input("Введите делимое: ")), var_2 = float(input("Введите делитель: "))):
    try:
        result = var_1 / var_2
        return result
    except ZeroDivisionError:
        return print("На ноль делить нельзя!")


print(my_division())
