from LinkedList.List import LinkedList
from Search.interpolate import int_polsearch

def int_polsearch_linkedlist(linked_list, x):
    array = linked_list.to_array()
    return int_polsearch(array, x)

# Create a linked list
ll = LinkedList()

ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
ll.add_last(40)
ll.add_last(50)

# Search for an element
result = int_polsearch_linkedlist(ll, 30)
print(result)  # Output: True

result = int_polsearch_linkedlist(ll, 60)
print(result)  # Output: False
