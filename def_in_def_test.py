def func1():
    def func2():
        print('test')

    return func2


a = func1()
print(a())
