def third(string: str) -> str:
    return string[2]


def penult(string: str) -> str:
    return string[-2]


def first_five(string: str) -> str:
    return string[:5]


def except_two_last(string: str) -> str:
    return string[:-2]


def odd_index(string: str) -> str:
    return string[::2]


def not_odd_index(string: str) -> str:
    return string[1::2]


def reversing(string: str) -> str:
    return string[::-1]


def reverse_in_one(string: str) -> str:
    return string[::-2]


def lenght(string: str) -> str:
    return len(string)


s = "1234567890"
print(third(s))
print(penult(s))
print(first_five(s))
print(except_two_last(s))
print(odd_index(s))
print(not_odd_index(s))
print(reversing(s))
print(reverse_in_one(s))
print(lenght(s))
