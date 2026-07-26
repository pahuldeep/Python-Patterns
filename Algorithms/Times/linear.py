
def get_sum(my_list):
    sum  = 0
    
    for item in my_list:
        sum += item
    return sum

array = [1, 2, 3, 4, 5]

result = get_sum(array)
print(result)