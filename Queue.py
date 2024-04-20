import SList

class Queue:
    def __init__(self):
        self.queue = SList.SList()
        self.count = 0
    
    def enqueue(self, item):
        self.queue.insert_back(item)
        self.count += 1 
    def dequeue(self):
        if self.count:
            dnode = self.queue.delete_front()
            self.count -= 1
            return dnode.item
        return None
    def print_queue(self):
        self.queue.print_list()

    
    
if __name__ == '__main__': 
    q = Queue()
    q.enqueue('mango')
    q.enqueue('apple')
    q.enqueue('orange')
    q.print_queue()
    print("삭제원소:", q.dequeue())
    q.print_queue()
    print("삭제원소:", q.dequeue())
    q.print_queue()
    print("삭제원소:", q.dequeue())
    q.print_queue()
    print("삭제원소:", q.dequeue())