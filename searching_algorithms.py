import math

def linear_search(to_search, to_find): # O(n)
    for i in range(len(to_search)):
        if to_search[i] == to_find:
            return i
    return None

def binary_search(to_search, to_find, min=None, max=None): # O(log(n)), requires a sorted list
    if min == None: min = 0
    if max == None: max = len(to_search) - 1
    split = (max - min) // 2
    if min == max: split = min # stops split from being 0 when min = max
    if split >= 0 and split < len(to_search):
        if to_find == to_search[split]: return split # found
        elif to_find < to_search[split]: # in left half
            max = split - 1
            return binary_search(to_search, to_find, min, max)
        elif to_find > to_search[split]: # in right half
            min = split + 1
            return binary_search(to_search, to_find, min, max)
        else:
            return None # item not present
    else:
        return None # item not present
    
def interpolation_search(to_search, to_find, min=None, max=None): # worst case O(n), average case O(log(n)), best case O(1), best with evenly distributed data
    if min == None: min = 0
    if max == None: max = len(to_search) - 1

    distance = to_find - to_search[min] # distance from min possible to wanted value
    if distance < 0: return None # wanted value less than minimum possible
    value_range = to_search[max] - to_search[min]
    if value_range != 0:
        fraction = distance / value_range # expected percent through the list we expect to find wanted value
    elif to_search[min] == to_find: return min # values are the same, hopefully it's the value we want
    else: return None
    
    split = math.floor(min + (fraction * (max - min)))
    print(min, max, distance, value_range, fraction, split)
    if split >= 0 and split < len(to_search):
        if to_find == to_search[split]: return split # found
        elif to_find < to_search[split]: # in left half
            max = split - 1
            return interpolation_search(to_search, to_find, min, max)
        elif to_find > to_search[split]: # in right half
            min = split + 1
            return interpolation_search(to_search, to_find, min, max)
        else:
            return None # item not present
    else:
        return None # item not present