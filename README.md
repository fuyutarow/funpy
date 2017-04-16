# FunPy

## install
```
pip install git+https://github.com/sktnkysh/funpy
```

## example
```python
from funpy import foldl, Map, printer, sider

foldl(1, [
  lambda a: a+2
  ])
// 3

Map([3,4],[
  lambda a:a+4
  ])
// [7, 8]

A = [2,3,4]
sider(A, A.append(5))
// [2, ,3, 4, 5]

foldl(0,[
    lambda x: x+1,
    lambda x: [x+3,x+4, x+10],
    lambda x: Map(x,[
        lambda a: a**2,
        ]),
    lambda x: printer(x),
    lambda x: sider(x, x.remove(121))
    ])
// [16, 25, 121]
// [16, 25]
```
