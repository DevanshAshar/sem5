class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.page_queue = []
    def page_fault(self, page):
        if page not in self.page_queue:
            if len(self.page_queue) == self.capacity:
                self.page_queue.pop(0)  # Remove the oldest page
            self.page_queue.append(page)
            return True  # Page fault occurred
        else:
            return False  # HIT
capacity = 3  
fifo_algorithm = FIFOPageReplacement(capacity)
page_requests = [1, 2, 3, 4, 1, 2, 5, 1, 2]
for page in page_requests:
    if fifo_algorithm.page_fault(page):
        print(f"Page {page} caused a page fault. Page frame: {fifo_algorithm.page_queue}")
    else:
        print(f"Page {page} is already in the memory. Page frame: {fifo_algorithm.page_queue}")
