class Queue:
  def __init__(self) -> None:
    self.queue = []

  def enqueue(self, val):
    self.queue.append(val)

  def dequeue(self):
    if self.queue:
      return self.queue.pop(0)
  
  


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)


print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())