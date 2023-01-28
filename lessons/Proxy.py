class Proxy:
    pass


class SingletonClass(object):
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonClass, cls).__new__(cls)
        return cls.instance(*args)


class Car:
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Car, cls).__new__(cls)
        return cls.instance(*args)

    def __init__(self, model = 'bugatti'):
        self.model = model

    def __str__(self):
        return f'I woke up in a new {self.model}'


if __name__ == '__main__':
    B = Car
    # M = Car('Mercedes')
    print(f'{B}')
    # print(f'{B = }')