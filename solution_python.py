class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = [self.value] # list of historical actions
        self.redos = [] # list of actions that could be redone

    def add(self, num: int):
        '''all historical actions are considered adds and so undoing them is just subtractions to value'''
        self.value += num
        self.history.append(num)

    def subtract(self, num: int):
        '''negative add'''
        self.add(-num)

    def undo(self):
        # check for possible undo actions
        if len(self.history) < 1:
            return
        last = self.history.pop()
        self.value -= last
        self.redos.append(last)

    def redo(self):
        # check for possible redo actions
        if len(self.redos) < 1:
            return
        nex = self.redos.pop()
        self.value += nex
        self.history.append(nex)

    def bulk_undo(self, steps: int):
        '''undo steps until history list is empty or required undos were performed'''
        for step in range(steps):
            if len(self.history) > 0:    
                self.undo()
            else:
                print("ran out of steps, undid {} steps instead")
                break


    def bulk_redo(self, steps: int):
        '''redo steps until redo list is empty or required redos were performed'''
        for step in range(steps):
            if len(self.redos) > 0:    
                self.redo()
            else:
                print("ran out of steps, redid {} steps instead")
                break