def deco(func):
    def helper(*args, **kwargs):
        helper.x += 1
        return func(*args, **kwargs)
    helper.x = 0
    helper.__name__ = func.__name__
    return helper


@deco
def f():
    if f.x == 1:
        f.y = 1
    else:
        f.y += 2
    return (f.x, f.y)

a = f()
print(a)

b = f()
print(b)

