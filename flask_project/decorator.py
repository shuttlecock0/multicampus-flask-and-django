def hello(func):
    def wrapper():
        print('HIHI')
        func()
        print('HIHI')
    return wrapper

@hello
def bye():
    print('BYEBYE')

bye()