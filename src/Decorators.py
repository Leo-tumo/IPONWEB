def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    return wrapper

@count_calls
def my_function():
    pass

my_function()
print(my_function.num_calls)
my_function()
print(my_function.num_calls)
my_function()
print(my_function.num_calls)