def optimized_bubble_sort(list):
    end = len(list) - 1
    for pass_number in range(end, 0, -1):
        swapped = False
        for idx in range(pass_number):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
                swapped = True
        if not swapped:
            break

    return list


def bubble_sort(list):
    end = len(list) - 1
    for pass_number in range(end, 0, -1):
        for idx in range(pass_number):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list

array = [23, 52, 12, 13 ,15, 11]
print(bubble_sort(array))


array = [45, 41, 12, 23 ,15, 11]
print(optimized_bubble_sort(array))