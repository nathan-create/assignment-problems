class Stack:
    def __init__(self):
        self.data=[]
    def push(self, item):
        self.data.append(item)
    def pop(self):
        del self.data[len(self.data)-1]
    def peek(self):
        return self.data[len(self.data)-1]

s = Stack()
print("testing Stack...")
assert s.data==[]
s.push('a')
s.push('b')
s.push('c')
assert s.data==['a','b','c']
s.pop()
assert s.data==['a','b']
s.peek()
assert s.data==['a','b']
print("Passed")