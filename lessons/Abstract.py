from abc import ABC,  abstractmethod


class Bird(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def walk(self):
        print(f'{self._name} can walk')


class FlyingBird(Bird):
    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        print(f"{self._name} eats mostly {self.ration}.")

    def fly(self):
        print(f'{self._name} can fly.')


class NonFlyingBird(Bird):
    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        print(f"{self._name} bird can swim.")

    def fly(self):
        raise AttributeError(f"'{self._name}' object has no attribute 'fly'")

    def eat(self):
        print(f"{self._name} eats mostly {self.ration}.")

    def __str__(self):
        return f"{self._name} bird can walk and swim."


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name):
        super().__init__(name)

    def fly(self):
        super(FlyingBird, self).fly()

    def __str__(self):
        return f"{self._name} bird can walk, swim and fly."


if __name__ == '__main__':

    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    try:
        p.fly()
    except AttributeError as e:
        print('AttributeError:', e)
    p.eat()
    c = FlyingBird("Canary")
    str(c)
    c.eat()
    s = SuperBird("Gull")
    print(SuperBird.__mro__)
    s.eat()
    s.fly()
    print(s)
