def shell_sort(elements):
    distance = len(elements) // 2
    while distance > 0:
        for i in range(distance, len(elements)):
            
            temp = elements[i]
            j = i

            while j >= distance and elements[j - distance] > temp:
                list[j] = elements[j - distance]
                j -= distance
                list[j] = temp

        distance //=2

    return elements

list = [21, 41, 22 ,32, 53, 23]
print(shell_sort(list))