my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = 50


if target in my_list:
    print(f'{target} is in the list')
else:
    print(f"{target} is not in the list")


def Linear_search(my_list, target):
    for i, value in enumerate(my_list):
        if value == target:
            return i
    return -1

print(Linear_search(my_list, target))
