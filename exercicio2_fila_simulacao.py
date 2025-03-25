class Queue:

    def __init__(self, queue = []):
        self.queue = queue
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop(0)


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)

print(queue.dequeue())