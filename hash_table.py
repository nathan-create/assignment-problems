class HashTable():
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for i in range(self.num_buckets)]
    
    def hash_function(self, string):
        indices = 'abcdefghijklmnopqrstuvwxyz'
        sum = 0
        for char in string:
            sum += indices.index(char)
        bucket = sum % self.num_buckets
        return bucket
    
    def insert(self, key, val):
        bucket = self.hash_function(key)
        self.buckets[bucket].append((key, val))

    def find(self, string):
        bucket = self.hash_function(string)
        for pair in self.buckets[bucket]:
            if pair[0] == string:
                return pair[1]


ht = HashTable(num_buckets = 3)
print("Testing init and hash hash function")
assert ht.buckets == [[], [], []]
assert ht.hash_function('cabbage') == 2
print("Passed")
print("Testing insert")
ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage',5)]]
ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]
ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]
ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]
print("Passed")
print("Testing find")
assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21
print("Passed")