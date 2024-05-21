class Fibonacci:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        item = self.a
        if item > self.start:
            raise  StopIteration
        self.a, self.b = self.b, self.a + self.b
        return item


obj = Fibonacci(15)

for i in obj:
    print(i)

