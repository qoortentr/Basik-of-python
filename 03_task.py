def type_logger(callback):
    def wrapper(*args):
        for i in args:
            print(str(callback.__name__) + '(' + str(i) + ':', str(type(callback(i))) + ')')
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3.2, 2, -1.3)
