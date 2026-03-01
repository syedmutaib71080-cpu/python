def debug(func):
    def wrapper(*args,**kwargs):
        args_value = ','.join(str(arg) for arg in args)
        kwargs_value = ','.join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling {func.__name__} with args: {args_value}, kwargs: {kwargs_value}")
        result = func(*args,**kwargs)
        return result
    return wrapper

@debug
def hello():
    print("Hello, world!")


@debug

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("mutaib",greeting="Hi")

hello()