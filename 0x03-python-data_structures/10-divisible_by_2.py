def divisible_by_2(my_list=[]):
    result_list = []

    for num in my_list:
        is_divisible = num % 2 == 0

    result_list.append(is_divisible)

    return result_list
