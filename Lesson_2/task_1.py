my_list = (123, 4.56, complex(2, 3), "abc", True, (1, 2), [3, 4], {5, 6}, None)
print("Мой список", my_list)
for ind, element in enumerate(my_list, 1):
    print(ind, "'элемент списка", element, "с типом", type(element))
