class MyRangeError(Exception):
    pass


class MyRange:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __repr__(self):
        return f'MyRange({self.current}, {self.end}, {self.step})'

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            tmp = self.current
            self.current += self.step
            return tmp

    def __len__(self):
        return (self.end - self.current) // self.step

    def __getitem__(self, index):
        """[] operator overload"""
        if index >= len(self):
            raise MyRangeError('Out of Range')
        return self.current + index * self.step

    def __reversed__(self):
        """reverse iterator"""
        current = self.end - self.step
        while current >= self.current:
            yield current
            current -= self.step
