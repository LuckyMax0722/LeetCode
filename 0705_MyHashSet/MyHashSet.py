class MyHashSet:

    def __init__(self):
        self.hash_table = []

    def add(self, key: int) -> None:
        if key not in self.hash_table:
            self.hash_table.append(key)

    def remove(self, key: int) -> None:
        if key in self.hash_table:
            self.hash_table.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hash_table:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)