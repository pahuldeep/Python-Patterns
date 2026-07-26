def linear_search(elements, item):
    
    index = 0
    found = False

    while index < len(elements) and found is False:
        
        if elements[index] == item:
            found = True
        else:
            index += 1
    
    return found

array = [1, 2, 3, 4, 5, 6, 7]

result = linear_search(array, 5)
print(result)