def merge_sort(elements):
    
    if len(elements) <= 1:
        return elements
    
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]

    merge_sort(left)
    merge_sort(right)

    a, b, c = 0, 0, 0

#   merge 2 halves
    while a < len(left) and b < len(right):
        if left[a] < right[b]:
            elements[c] = left[a]
            a += 1

        else:
            elements[c] = right[b]
            b+=1
        c+=1

#   left 
    while a < len(left):
        elements[c] = left[a]
        a += 1
        c += 1

#   right
    while b < len(right):
        elements[c] = right[b]
        b += 1
        c += 1

    return elements

