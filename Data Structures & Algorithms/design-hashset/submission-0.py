class MyHashSet:

    def __init__(self):
        self.data = [[]]
        self.size = 0
        self.capacity = 1

    def hash(self, key: int) -> int:
        return key % self.capacity
    
    def grow(self) -> None:
        new_data = []
        self.capacity *= 2
        for i in range(self.capacity):
            new_data.append([])
        for l in self.data:
            for n in l:
                new_data[self.hash(n)].append(n)
        self.data = new_data

    def add(self, key: int) -> None:
        if not self.contains(key):
            if self.size >= self.capacity:
                self.grow()
            self.data[self.hash(key)].append(key)
            self.size += 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[self.hash(key)].remove(key)
            self.size -= 1

        

    def contains(self, key: int) -> bool:
        return key in self.data[self.hash(key)]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)