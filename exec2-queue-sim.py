class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def deque(self):
        self.queue.pop(0)

    def print_queue(self):
        for i in self.queue:
            print(i)

queue = Queue()
queue.enqueue(2)
queue.enqueue(1)
queue.deque()
queue.print_queue()
