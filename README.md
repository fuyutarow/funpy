# FunPy

## install
```
pip install git+https://github.com/sktnkysh/funpy
```

## example
```python
from funpy import seq, each, printer, sider
from functools import reduce

seq(1, [
  lambda a: a+2
  ])
// 3

each([3,4],[
  lambda a:a+4
  ])
// [7, 8]

A = [2,3,4]
sider(A, A.append(5))
// [2, ,3, 4, 5]

seq(0,[
    lambda x: x+1,
    lambda x: [x+3,x+4, x+5, x+7],
    lambda x: each(x,[
      lambda a: a**2,
      ]),
    lambda x: printer(x),
    lambda x: sider(x, x.remove(64)),
    lambda x: reduce(lambda a,b: a+b, x),
    ])
// [16, 25, 36, 64]
// 77
```
