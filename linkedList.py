class Cell:
    value = None
    next = None

    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next
    def __str__(self):
        return f"{self.value}"
    def get(self):
        return self.value
    def get_next(self):
        return self.next