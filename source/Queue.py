class Queue:
    def __init__(self,SizeOfQueue) -> None:
        self.queue_array = [None] * SizeOfQueue
        self.head = 0
        self.tail = 0
        self.maximum = len(self.queue_array) - 1

    def enqueue(self,new_value):
        if (self.head == 1 and self.tail == self.maximum) or (self.head == self.tail + 1):
            print("Error-queue is full")
        else:
            self.queue_array[self.tail] = new_value
            self.tail = self.tail + 1

    def dequeue(self):
        print(self.queue_array)
        if self.head == self.tail-1:  # EMLYN: Require 1 entry remain
            output = self.queue_array[self.head]
        else:
            output = self.queue_array[self.head]
            self.head +=1
        return output
