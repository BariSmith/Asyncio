def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner


class BlaBlaException(Exception):
    pass



#@coroutine
def subgen():
    while True:
        try:
            massage = yield
        except StopIteration:
            print('Harosh!')
            break
        else:
            print('..............', massage)

    return 'returned from subgen()'



@coroutine
def delegator(g):
    #while True:
     #   try:
      #      data = yield
       #     g.send(data)
        #except BlaBlaException as e:
         #   g.throw(e)
    result = yield from g
    print(result)


