test_num = "6489319447155620"


def validate(num: str):
    for index in range(len(num)):
        num_list[index] = int(num[index])


num_list = list(test_num)
print(num_list)
print(len(num_list))

print(validate(test_num))
num_list = list(test_num)
num_list.pop()
print(num_list)


def reverse_test_num(string):
    return string[::-1]


print(reverse_test_num("6489319447155620"))
