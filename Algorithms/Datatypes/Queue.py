class ListQueue(object):

   def __init__(self):
      self.items = []

   def isEmpty(self):
      return self.items == []
   
   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
      return self.items.pop()

   def size(self):
      return len(self.items)
   

class StackQueue:

   def __init__(self):
      self.in_stack = []
      self.out_stack = []

   def enqueue(self, data):
      self.in_stack.append(data)

   def dequeue(self):
      if not self.out_stack:
         while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
      return self.out_stack.pop()
   
