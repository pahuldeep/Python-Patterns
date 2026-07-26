def search_binary(my_list, item):
    first, last = 0, len(my_list) - 1
    found_flag = False
    while first <= last and not found_flag:
        mid = (first + last) // 2
        if my_list[mid] == item:
            found_flag = True
        else:
            if item < my_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found_flag

my_list = [3, 2, 1]

result = search_binary(my_list, 2)

if result:
    print("Element found in the list.")
else:
    print("Element not found in the list.")
