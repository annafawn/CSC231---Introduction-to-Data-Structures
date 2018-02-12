class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #result = self.items[-1]
        #self.items = self.items[:-1]
        #return result

        #return self.items.pop()

        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]
        #reutrn self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)