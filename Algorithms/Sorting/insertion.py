def insertion_sort(elements):

    for index in range(1, len(elements)):
        j = index - 1
        next = elements[index]

        while j >= 0 and elements[j] > next:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = next

    return elements

array = [12, 41, 15, 51, 56]
print(insertion_sort(array))