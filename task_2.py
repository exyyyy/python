time = int(input("Введите время в секундах"))
ss = time % 60
hh = time // 3600
mm = (time - (hh * 60)) // 60
print(hh, ":", mm, ":", ss)
