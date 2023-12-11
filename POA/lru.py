from collections import OrderedDict
class LRUPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_order = OrderedDict()
    def check_page_fault(self, page): 
        if page in self.page_order: #HIT
            self.page_order.move_to_end(page)          
            return False  
        else:
            if len(self.page_order) == self.capacity:
                self.page_order.popitem(last=False) #last=False rakhenge toh FIFO order mein pop hoga
            self.page_order[page] = None #dict hai isliye key ke saath kuch value assign karna padega
            return True  # Page fault occurred
capacity = 3 
lru_algorithm = LRUPageReplacement(capacity)
page_requests = [1,2, 3, 4, 1, 2, 5, 1, 2]
for page in page_requests:
    if lru_algorithm.check_page_fault(page):
        print(f"Page {page} caused a page fault. Page order: {list(lru_algorithm.page_order.keys())}")
    else:
        print(f"Page {page} is already in the memory HIT . Page order: {list(lru_algorithm.page_order.keys())}")
