# Вариант 1

monthes = "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"
n = int(input("Введите номер месяца (от 1 до 12): "))
print("Вы ввели", monthes[n-1])


# Вариант 2

monthes = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август", 9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
n = int(input("Введите номер месяца (от 1 до 12): "))
print("Вы ввели", monthes.get(n))
