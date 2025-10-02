# When to use:
# insertion sort: small lists
# selection sort: small lists
# quick sort: list does not contain many duplicates
# heap sort: less than ideal list makeup for other sorting methods
# merge sort: if you don't have memory restrictions
# bubble sort: small lists, lists that are mostly sorted
# counting sort: list is made up of a restricted range of integers

class InsertionSortedList:
    list = []

    def __init__(self, init_list=[]): # O(n^2)
        if len(init_list) > 1: # init_list needs to be sorted
            self.list.append(init_list.pop()) # initialize list with value from init_list
            while len(init_list) > 0: # continue through init_list
                for j in range(len(self.list) + 1): # check each value in list
                    if j == len(self.list): # next item greater than all other items in list
                        self.list.append(init_list.pop(0))
                        break # position found
                    elif init_list[0] > self.list[j]: # next item belongs after this item in list
                        continue # continue looking for position
                    elif init_list[0] <= self.list[j]: # next item begins before this item in list
                        self.list.insert(j, init_list.pop(0))
                        break # position found
        else:
            self.list = init_list
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)
    
class SelectionSortedList:
    list = []

    # TODO: inplace selection sort implemetation
    def __init__(self, init_list=[]): # O(n^2)
        if len(init_list) > 1:
            while len(init_list) > 0:
                smallest_index = 0
                for i in range(len(init_list)):
                    if init_list[i] < init_list[smallest_index]: # new smallest item
                        smallest_index = i
                self.list.append(init_list.pop(smallest_index)) # append smallest item
        else:
            self.list=init_list
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)
    
class QuickSortedList:
    list = []

    def __init__(self, init_list=[]): # inplace quicksort, worst case O(n^2), random case O(nlog(n))
        if len(init_list) > 1:
            self.list = self.quicksort(init_list)
        else:
            self.list = init_list
    def quicksort(self, list):
        if len(list) <= 1:
            return list
        divider = list[0] # use first item to divide into sublists
        hole_i = 0 # keep track of where the "hole" is
        left_i = 1 # leftmost unsorted item
        right_i = len(list) - 1 # rightmost unsorted item
        while left_i <= right_i: # if indexes have not crossed
            if hole_i < right_i: # "hole" is on the left
                if list[right_i] < divider: # item should be moved to "hole" on left side of list
                    list[hole_i] = list[right_i]
                    hole_i = right_i
                    right_i -= 1 # move right index towards left
                else: # item is already on correct side of list
                    right_i -= 1 # move right index towards left
            else: # "hole" is on the right
                if list[left_i] > divider: # item should be moved to "hole" of right side of list
                    list[hole_i] = list[left_i]
                    hole_i = left_i
                    left_i += 1 # move left index towards right
                else: # item is already on correct side of list
                    left_i += 1 # move left index towards right
        list[hole_i] = divider
        list[:hole_i] = self.quicksort(list[:hole_i]) # sort everything before the divider
        list[hole_i+1:] = self.quicksort(list[hole_i+1:]) # sort everything after the divider
        return list
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)
    
class HeapSortList:
    heap = []

    def __init__(self,init_heap=None):
        if len(init_heap) > 1:
            # initial sort O(nlog(n))
            for item in init_heap:
                self.insert(item)
        else:
            self.heap=init_heap
    def __str__(self):
        print(self.heap)
        return str(self.get())
    def get(self): # returns heap sorted list, O(nlog(n))
        sorted_list = [self.heap.pop(0)] # root is always largest
        while len(self.heap) > 0:
            self.heap.insert(0, self.heap.pop()) # move last leaf to root
            is_heap = False
            parent_i = 0
            while not is_heap: # push root down until heap requirements are satisfied
                child_i = ((parent_i + 1) * 2) - 1 # get index for left child
                if child_i < len(self.heap) and child_i >= 0: # if left child exists
                    if child_i + 1 < len(self.heap): # if right child exists
                        if self.heap[child_i + 1] > self.heap[child_i]:
                            child_i += 1 # child_i should point to largest child
                    if self.heap[child_i] > self.heap[parent_i]: # swap child and parent if child is larger
                        parent = self.heap[parent_i]
                        self.heap[parent_i] = self.heap[child_i]
                        self.heap[child_i] = parent
                        parent_i = child_i
                    else: # children are smaller than parent
                        is_heap = True
                else: # no more children
                    is_heap = True
            sorted_list.insert(0, self.heap.pop(0)) # root is always largest
        return sorted_list
    def insert(self,value): # O(log(n))
        self.heap.append(value) # add to end of heap
    
        # swap value with parent until the parent is bigger than the child to satisfy heap requirement
        is_heap = False
        value_i = len(self.heap) - 1
        while not is_heap:
            parent_i = ((value_i + 1) // 2) - 1 # inflate for integer division, then deflate
            print(self.heap)
            print(value_i, parent_i)
            if parent_i >= 0: # if parent_i exists
                if self.heap[value_i] > self.heap[parent_i]: # swap parent and child
                    self.heap[value_i] = self.heap[parent_i]
                    self.heap[parent_i] = value
                    value_i = parent_i
                else:
                    is_heap = True
            else:
                is_heap = True

class MergeSortedList:
    list = []

    def __init__(self, init_list=[]):
        if len(init_list) > 1:
            self.list = self.mergesort(init_list)
        else:
            self.list = init_list
    def mergesort(self, list): # O(nlog(n)), but requires memory to hold left, right, and merged arrays
        if len(list) <= 1: # list sorted
            return list
        
        # split list a recursively sort left and right sections
        split_i = len(list) // 2
        left = self.mergesort(list[:split_i])
        right = self.mergesort(list[split_i:])
        merged = []
        while len(left) > 0 or len(right) > 0: # while there are items to sort
            if len(left) > 0:
                if len(right) > 0:
                    if left[0] < right[0]: # left list has smallest item
                        merged.append(left.pop(0))
                    else: # right list has smallest item
                        merged.append(right.pop(0))
                else: # left list has remaining items
                    merged.append(left.pop(0))
            else: # right list has remaining items
                merged.append(right.pop(0))
        return merged
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)

class BubbleSortedList:
    list = []

    # TODO: only scan sections of the list not yet sorted
    def __init__(self, init_list=[]): # O(k*n), worst case O(n^2) if k (farthest move) = n, faster than mergesort/heapsort/quicksort if k < log(n)
        if len(init_list) > 1:
            bubble_sorted = False
            while not bubble_sorted: # continue until list is sorted
                swapped = False
                for i in range(len(init_list) - 1): # increment through list
                    if init_list[i] > init_list[i+1]: # if out of order, swap
                        i_value = init_list[i]
                        init_list[i] = init_list[i+1]
                        init_list[i+1] = i_value
                        swapped = True
                if not swapped: # no swaps required, so sorted
                    bubble_sorted = True
                    break

                # backwards bubble sort to speed big moves up the array
                swapped = False
                for i in range(len(init_list) - 1): # increment through list
                    i = len(init_list) - 1 - i # swap index to end
                    if init_list[i] < init_list[i-1]: # if out of order, swap
                        i_value = init_list[i]
                        init_list[i] = init_list[i-1]
                        init_list[i-1] = i_value
                        swapped = True
                if not swapped: # no swaps required, so sorted
                    bubble_sorted = True
            self.list = init_list
        else:
            self.list = init_list
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)
    
class CountingSortedList: # sorting fixed range of integers
    list = []

    def __init__(self, init_list=[], min_max=(0,10)): # O(n + m) where m is the difference between the min and max
        if len(init_list) > 1:
            counts = [0] * (min_max[1] - min_max[0]) # initialize array of zeros of size = difference btwn min and max (could also use np.zeros)
            
            # count how many times each value occurs in list
            for item in init_list:
                counts[item-min_max[0]] += 1

            # overwrite list with values based on count
            list_i = 0
            for counts_i in range(len(counts)):
                for c in range(counts[counts_i]):
                    init_list[list_i] = counts_i + min_max[0]
                    list_i += 1
            
            self.list = init_list
        else:
            self.list = init_list
    def __str__(self):
        return str(self.list)
    def insert(self, value): # O(n)
        for i in range(len(self.list) + 1):
            if i == len(self.list): # next item greater than all other items in list
                self.list.append(value)
                break # position found
            elif value > self.list[i]: # next item belongs after this item in list
                continue # continue looking for position
            elif value <= self.list[i]: # next item begins before this item in list
                self.list.insert(i, value)
                break # position found
    def pop(self, index):
        return self.list.pop(index)