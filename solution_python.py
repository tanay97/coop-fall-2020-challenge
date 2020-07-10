class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.history = []
        self.index = 0
        self.history.append(self.value)

    def add(self, num: int):
        self.value += num
        self.history.append(self.value)
        self.index += 1

    def subtract(self, num: int):
        self.value -= num
        self.history.append(self.value)
        self.index += 1

    def undo(self):
        if self.index == 0:
            return
        self.index -= 1
        self.value = self.history[self.index]

    def redo(self):
        if self.index == len(self.history) - 1:
            return
        self.index += 1
        self.value = self.history[self.index]

    def bulk_undo(self, steps: int):
        self.index = max(0, self.index - steps)
        self.value = self.history[self.index]

    def bulk_redo(self, steps: int):
        self.index = min(len(self.history) - 1, self.index + steps)
        self.value = self.history[self.index]
