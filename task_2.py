time = int(input("Введите время в секундах: "))
ss = time % 60
hh = time // 3600
mm = hh * -60 + time // 60
if ss < 10:
    ss = "0" + str(ss)
else:
    ss = str(ss)
if mm < 10:
    mm = "0" + str(mm)
else:
    mm = str(mm)
if hh < 10:
    hh = "0" + str(hh)
else:
    hh = str(hh)
print("Время в формате чч:мм:сс будет {:s}:{:s}:{:s}".format(hh, mm, ss))
