class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True
