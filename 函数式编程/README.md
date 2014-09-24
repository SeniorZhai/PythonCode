##函数做参数
函数本身可以作为参数传入函数
`map`函数接收两个参数，一个函数，一个序列，`map`将传入的序列的元素依次传入到函数中

![](./0.png)
```python
def f(x):
	print x*x

map(f,range(1,10))
```
##排序
`sorted()`函数可以对list进行排序
```python
l = [2,3,1,32,11,34,12]
print sorted(l)
```
`sorted`是高阶函数，可以接收一个比较函数来实现自定义排序
```python
def cmp(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	return 0

print sorted([2,3,1,32,11,34,12],cmp)
```

##函数作为返回值
