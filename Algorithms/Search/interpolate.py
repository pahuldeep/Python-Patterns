def int_polsearch(list, x):

    first, last = 0, (len(list) - 1)
    
    while first <= last and x >= list[first] and list[last]:

        mid = first + int(((float(last - first)) / (list[last] - list[first])) * (x - list[first]))

        if mid < 0 or mid >= len(list): # valid range
            return False
        
        if list[mid] == x:
            return True
        
        if list[mid] < x:
            first = mid + 1
        else:
            last = mid - 1

    return False