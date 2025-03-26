class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def deque(self):
        self.queue.pop(0)

    def print_queue(self):
        for i in self.queue:
            print(i)

    def print_reverse_queue(self):
        stack = []
        for i in self.queue:
            stack.append(i)
        while stack:
            print(stack.pop(), end=', ')
        print()

queue = Queue()
numbers_input = input("Insira os números (separado por vírgula e espaço): ")

for i in numbers_input.split(", "):
    queue.enqueue(int(i))

    queue.print_reverse_queue()