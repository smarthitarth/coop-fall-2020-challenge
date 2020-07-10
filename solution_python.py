class EventSourcer():
    # Do not change the signature of any functions
    


    def __init__(self):
        self.value = 0
        self.memory = []
        self.curr_pos = 0
        self.memory.append(self.value)

    def add(self, num: int):
        self.value += num
        self.curr_pos+=1
        self.memory.append(self.value)
        
        
        print(self.memory)

    def subtract(self, num: int):
        
        self.value -= num
        self.curr_pos+=1
        self.memory.append(self.value)
        print(self.memory)

    def undo(self):
        if self.curr_pos-1 <= 0:
            self.curr_pos = 0
            self.value = 0
        else:
            self.value = self.memory[self.curr_pos-1]
        #self.memory.append(self.curr_pos)
        print(self.memory)

    def redo(self):
        if(self.curr_pos+1 < len(self.memory)):
            self.curr_pos += 1
        self.value = self.memory[self.curr_pos]
        print(self.memory)

    def bulk_undo(self, steps: int):
        self.curr_pos -= steps
        if(self.curr_pos < 0):
            self.value = self.memory[0]
        else:
            self.value = self.memory[self.curr_pos]
        print(self.memory)


    def bulk_redo(self, steps: int):
        self.curr_pos += steps
        if self.curr_pos + 1 >= len(self.memory):
            self.curr_pos = len(self.memory)-1
        self.value = self.memory[self.curr_pos]

        print(self.memory)

