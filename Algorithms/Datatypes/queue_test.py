from Queue import ListQueue
from Queue import StackQueue

list_queue = ListQueue()

list_queue.enqueue('Red')
list_queue.enqueue('Green')
list_queue.enqueue('Yellow')

print("Size: ", list_queue.size())
print(list_queue.dequeue())


stack_queue = StackQueue()

stack_queue.enqueue(5)
stack_queue.enqueue(6)
stack_queue.enqueue(7)

print("Before: ", stack_queue.in_stack)
stack_queue.dequeue()
print("After: ", stack_queue.in_stack)

print(stack_queue.out_stack)
stack_queue.dequeue()
print(stack_queue.out_stack)
