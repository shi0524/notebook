
# inspect 谁调用了我

```
当程序出现诡异的bug时，我们需要层层去跟踪，尤其是要理清顺序。
这时如果有个清晰的调用脉络调试就容易多了。
利用inspect模块的getframeinfo方法来实现这需求。
```

import inspect
def foo():
    who = inspect.getframeinfo(inspect.currentframe().f_back)v
    print '{} call me'.format(who)
 
def a():
    foo()
 
def b():
    foo()
 
a()
b()
a()
