def count_calls(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper

@count_calls
def foo():
    pass

foo()
print(foo.calls)
foo()
print(foo.calls)
foo()
print(foo.calls)