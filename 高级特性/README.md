#切片
list、tuple可以作切片处理
```python
L = range(101)
print L
print L[0:10]
print L[:20]
print L[49:70] #取49开始到70，不包括70
print L[-2] #取倒数第二个
print L[:10:2] #取10个，每2个一取

print (1,2,3,4,5)[:3]
print 'ABCDEFG'[::2]
```

#迭代
```python
sum = 0
for n in L:
	sum += n
print sum
```
dict也可以迭代
```python
d = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

for value in d.itervalues():
	print value

for key,value in d.iteritems():
	print key ,':',value
```
判断是否可以迭代，通过collection模块中的Iterable类型判断
```python

from collections import Iterable

print isinstance('abc',Iterable)
print isinstance('[1,2,3]',Iterable)
print isinstance(123,Iterable)

```

`enumerate`函数可以把一个list变成`索引-元素`对
```python
for x,y in [(1,2),(2,4),(3,9)]:
	print x,y
```

##列表生成式
```python
print [x * x for x in range(1,11)]
print [m + n for m in 'ABC' for n in 'XYZ']

import os
print [d for d in os.listdir('.')] #当前目录所有文件盒目录
```

##生成器Generator
```python
g = (x * x for x in range(10000000)) #写法上与列表生成器仅仅是()和[]的不同
for n in g:
	print n
```