test_num = "6489319447155620"


def validate(num: str):
    for index in range(len(num)):
        int_version = int(num[index])



print(validate(test_num))
num_list = list(test_num)
num_list.pop(15)
print(num_list)


def reverse_test_num(string):
    return string[::-15]

