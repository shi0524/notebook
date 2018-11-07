
# Python 将字典和列表做成只读属性

### 只读字典
```
class ReadonlyDict(dict):

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError('cantnot modify readonly dict')
    __setitem__ = __readonly__
    __delitem__ = __readonly__
    pop = __readonly__
    popitem = __readonly__
    clear = __readonly__
    setdefault = __readonly__
    del __readonly__
```

### 只读列表
```
class ReadonlyList(list):
    """ 防止操作过程中更改配置
    """

    def __readonly__(self, *args, **kwargs):
        raise RuntimeError('cantnot modify readonly list')

    __setitem__ = __readonly__
    __delitem__ = __readonly__
    __iadd__ = __readonly__
    __imul__ = __readonly__
    pop = __readonly__
    append = __readonly__
    extend = __readonly__
    insert = __readonly__
    remove = __readonly__

    del __readonly__
```


### 将字典和列表转换成只读
```
def make_readonly(x, deep=0):
    if x.__class__ is list:
        d = []
        for i in x:
            d.append(make_readonly(i, deep+1))
        return ReadonlyList(d)
    elif x.__class__ is dict:
        d = {}
        for k, v in x.iteritems():
            d[k] = make_readonly(v, deep+1)
        return d if deep else ReadonlyDict(d)
    return x
```

