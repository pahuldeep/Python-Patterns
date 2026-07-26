def selection_sort(list):
    for slot in range(len(list)-1, 0, -1):
        max_index = 0
        for location in range(1, slot+1):
            if list[location] > list[max_index]:
                max_index = location

        list[slot], list[max_index] = list[max_index], list[slot]
    return list
    


array = [12, 41, 23, 11 ,123, 8]
print(selection_sort(array))
