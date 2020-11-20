class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self, item):
        self.data.append(item)
    def dequeue(self):
       del self.data[0]
    def peek(self):
        return self.data[0]

q= Queue()
assert q.data==[]
print("Passed")


q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
assert q.data==['a','b','c']
print("Passed")


q.dequeue()
assert q.data==['b','c']
print("Passed")


print(q.data[0])
assert q.peek()== 'b'
print("Passed")


assert q.data==['b','c']
print("Passed")