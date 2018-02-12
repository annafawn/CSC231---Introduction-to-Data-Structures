class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)

    def remove_rear(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)