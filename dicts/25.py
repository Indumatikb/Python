class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}   # store key → value
        self.order = []   # store usage order

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)   # remove old position
            self.order.append(key)   # make it recent
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            old = self.order.pop(0)   # remove oldest
            del self.cache[old]

        self.cache[key] = value
        self.order.append(key)


# 🔥 Calling functions
obj = LRU(2)   # capacity = 2

obj.put(1, 10)   # cache = {1:10}
obj.put(2, 20)   # cache = {1:10, 2:20}

print(obj.get(1))  # 10 → now 1 becomes recent

obj.put(3, 30)   # removes 2 (oldest)

print(obj.get(2))  # -1 (not found)
print(obj.get(3))  # 30