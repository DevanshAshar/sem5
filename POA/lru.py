from collections import OrderedDict
def lru_page_replacement(capacity, page_requests):
    page_order = OrderedDict()
    for page in page_requests:
        if page in page_order:  # HIT
            page_order.move_to_end(page)
            print(f"Page {page} is already in the memory=> HIT")
        else:
            if len(page_order) == capacity:
                page_order.popitem(last=False)  #last=False rakhenge toh FIFO order mein pop hoga
            page_order[page] = None #dict hai isliye key ke saath kuch value assign karna padega
            print(f"Page {page} caused a page fault. Page order: {list(page_order.keys())}")
lru_page_replacement(capacity = 3, page_requests = [1, 2,1, 3, 4, 1, 2, 5, 1, 2,7])
