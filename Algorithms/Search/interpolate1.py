def interpolation_search(list, target):

  low, high = 0, len(list) - 1

  while low <= high:
    
    if list[high] == list[low]: return low if list[low] == target else -1 
    
    pos = low + int(((float(high - low)) / (list[high] - list[low])) * (target - list[low]))

    if pos < low or pos > high: 
      pos = low if target < list[low] else high 

    if list[pos] == target: return pos
    
    elif list[pos] < target:
      low = pos + 1
    else:
      high = pos - 1

  return -1

# Example usage with sample list
list = [2, 12, 21, 44, 53, 56]
sortedlist = sorted(list)
print(sortedlist)

target = int(input("Enter Target: "))

result = interpolation_search(list, target)

if result != -1:
  print(f"Target {target} found at index {result}")
else:
  print(f"Target {target} not found in the list")
