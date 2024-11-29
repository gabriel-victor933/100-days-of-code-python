def logging_decorator(function):
    
    def wrapper(*args):
        result = ", ".join(map(str, args))
        print(f'You called {function.__name__}({result})')
        print(f'It returned: {function(*args)}')
        
    return wrapper
    

# TODO: Use the decorator 👇

@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)