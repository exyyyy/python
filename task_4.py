n = int(input("Введите целое положительное число: "))
m = 0
while  n > 0:
    last = n % 10
    if last > m:
        m = last
    n = n // 10
print("Максимальная цифра в числе ", m)
