def val_checker(callback):
    def wrapper(*args):
        for i in args:
            if i < 0:
                raise ValueError(f'wrong val {i}')
            else:
                print(callback(i))
    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5, -5, 4)