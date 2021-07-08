from dataclasses import dataclass

@dataclass
class FibIterator:
    max_n : int = 0

    def __post_init__(self):
        self.n, self.a, self.b = 0, 0 , 1


    def __iter__(self):
        return self

    def __next__(self):
        self.n += 1
        self.a,self.b = self.b, self.a + self.b #b future value
        if not self.max_n or self.n <= self.max_n:
            return self.a
        else:
            raise StopIteration
