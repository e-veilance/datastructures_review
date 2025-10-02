import collections

class Stack:
    stack = [] # use list as base for stack

    def __init__(self, init_stack=[]):
        self.stack = init_stack
    def push(self, value):
        self.stack.append(value) # add value to end
    def pull(self):
        return self.stack.pop() # remove last item from stack
    
class ListQueue:
    # lists are inefficient for queues as they require all list items to be shifted
    # when removing from the start of the list
    queue = [] # use list as base for queue

    def __init__(self, init_queue=[]):
        self.queue = init_queue
    def push(self, value):
        self.queue.append(value) # add value to end
    def pull(self):
        return self.queue.pop(0) # remove first item from queue
    
class DequeQueue:
    # deques are more efficient than stacks as they are made to have fast insertion/deletion
    # from the beginning of the deque
    queue = collections.deque()

    def __init__(self, init_queue=collections.deque()):
        self.queue = init_queue
    def push(self, value):
        self.queue.append(value) # add value to end
    def pull (self):
        return self.queue.popLeft() # remove first value from queue