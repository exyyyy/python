"""def user_data(name, surname, birth_year, living_city, email, phone_number):"""
def print_user_data(**kwargs):
    print("Словарь:")
    print(kwargs)
    print()
    print("Строка:")
    print(" ".join(str(e) for e in list(kwargs.values())))
    return


print_user_data(name = "Алексей", surname = "Михеев", birth_year = 1989, living_city = "Kazan", email = "noname@gmail", phone_number = "+79000000000")
