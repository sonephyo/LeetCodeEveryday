class OrderedSetPython:
    def __init__(self):
        self.set = []

    def add(self, element):
        if element not in self.set:
            self.set.append(element)
            self.set.sort(reverse=True)

    def find_by_order(self, k):
        if k < 0 or k >= len(self.set):
            return None
        return self.set[k]

    def order_of_key(self, element):
        return sum(1 for x in self.set if x > element)

orderedSet = OrderedSetPython()
orderedSet.add(5)
orderedSet.add(1)
orderedSet.add(2)

print(orderedSet.find_by_order(1))  # Find 2nd element in descending order
print(orderedSet.order_of_key(3))   # Elements greater than 3 in descending order
