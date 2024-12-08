class Queue:
    def __init__(self):
        self.queue = []

    def insert(self, value):
        self.queue.append(value)

    def pop(self):
        if len(self.queue) == 0:
            print("Warning: queue is empty")
            return None
        return self.queue.pop(0)

my_queue = Queue()
my_queue.insert(10)
my_queue.insert(20)
my_queue.insert(30)

print("after insert", my_queue.queue)

popped = my_queue.pop()

print("after delete", my_queue.queue)
 
#######################################

class QueueRound2:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.queue = []
    def insert(self, value):
        if len(self.queue) >= self.size:
            print(f"queue {self.name} is full.")
        else:
            self.queue.append(value)
    def pop(self):
        if len(self.queue) == 0:
            print(f"queue {self.name} is empty.")
            return None
        return self.queue.pop(0)
    
queue1 = QueueRound2("queue1", 3)
queue2 = QueueRound2("queue2", 5)

queue1.insert(10)
queue1.insert(20)
queue1.insert(30)
queue1.insert(40)

queue2.insert(100)
queue2.insert(200)
queue2.insert(300)

print(queue1.queue)
print(queue2.queue)