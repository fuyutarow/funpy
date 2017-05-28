from functools import reduce, partial
seq = lambda a,fff:\
    reduce(lambda f,g: partial(lambda f,g,h: f(g(h)), f, g),fff[::-1])(a)
each = lambda A,fff: [ seq(a,fff) for a in A]
def printer(a):
    print(a)
    return a
def sider(a,f):
    f
    return a
