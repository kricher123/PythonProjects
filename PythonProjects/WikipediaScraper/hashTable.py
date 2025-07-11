class hashTable(object):
    def __init__(self, size=10000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value
    
    def insert(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] += 1
                return
        self.table[index].append([key , 1])

    def contains(self, key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return True
        return False
    









# class hashTable(object):
#     def __init__(self, size=100):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hash(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self.hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 pair[1] = value
#                 return
#         self.table[index].append([key, value])

#     def get(self, key):
#         index = self.hash(key)
#         for pair in self.table[index]:
#             if pair[0] == key:
#                 return pair[1]
#         return None

#     def __str__(self):
#         return str(self.table)