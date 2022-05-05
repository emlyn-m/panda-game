class Stack:

    def __init__(self,SizeOfStack) -> None:
        self.stack_array = [None] * SizeOfStack
        self.TOS = -1
        self.Maximum = len(self.stack_array) - 1

    def push(self,new_item):
        if self.TOS == self.Maximum:
            print("Stack is full")
        else:
            self.TOS = self.TOS + 1
            self.stack_array[self.TOS] = new_item

    def pop(self):
        if self.TOS == -1:
            print("Stack is empty")
        else:
            outcome = self.stack_array[self.TOS]
            self.TOS -=1

            return outcome

    def peek(self):
        if self.TOS == -1:
            print("Stack is empty")
        else:
            outcome = self.stack_array[self.TOS]

            return outcome
