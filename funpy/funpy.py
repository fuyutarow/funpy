from functools import reduce, partial
foldl = lambda a,fff:\
    reduce(lambda f,g: partial(lambda f,g,h: f(g(h)), f, g),fff[::-1])(a)
Map = lambda A,fff: [ foldl(a,fff) for a in A]
def printer(a):
    print(a)
    return a
def sider(a,f):
    f
    return a
