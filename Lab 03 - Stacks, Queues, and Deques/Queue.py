class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        #self.items.insert(0, item)

    def dequeue(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop(0)
        #self.items.

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)