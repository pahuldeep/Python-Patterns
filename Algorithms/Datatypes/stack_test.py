from Stack import Stack

stack = Stack()

stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')

print(stack.peek())
print(stack.size())
print("Stack is Empty: ", stack.isEmpty())

stack.pop()
stack.pop()
stack.pop()
stack.pop()

print("Stack is Empty: ", stack.isEmpty())