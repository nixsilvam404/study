def print_numbers(some_list: list):
    for i in some_list:
        if i % 5 == 0 and i < 150:
            print(i)


list_of_six = list(range(100, 197, 6))
# print(list_of_six)
print_numbers(list_of_six)

