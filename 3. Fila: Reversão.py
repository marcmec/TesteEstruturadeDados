class Queue:
  def __init__(self) -> None:
    self.queue = []

  def enqueue(self, val):
    self.queue.append(val)

  def dequeue(self):
    if self.queue:
      return self.queue.pop(0)

def reverse(queue):
  reversed = []
  for i in range(len(queue.queue) - 1, -1, -1):
    reversed.append(queue.queue[i])
  return reversed

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(reverse(q))