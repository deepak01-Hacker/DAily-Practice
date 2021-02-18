#User function Template for python3

# design the class in the most optimal way

from collections import OrderedDict 

class LRUCache:
        
    def __init__(self,cap):
        self.cache = OrderedDict()
        self.capacity = cap

    
    #This method works in O(1)
    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
        
        
    #This method works in O(1)   
    def set(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)



