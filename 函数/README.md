#定义
```python
def fun():
	pass
```
定义了一个空函数
##可变参数
参数会被包装成tuple
```python
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = n * n + sum
	retrun sum
calc()
calc(1,2)
# python允许在list或tuple前面加*，把list或tuple的元素变成可变参数传进去
calc(*(1,2,3))
```
##关键字参数
关键字参数允许传入0个或任意个含参数名的参数，这些参数在函数内部自动组装为一个dict
```python 
def person(name,age,**kw):
	print 'name:',name," age:",age,'other:',kw

person('Bob',32,city="Beijing")
```

##参数组合
Python中函数可以用`必选参数`、`默认参数`、`可变参数`、`关键字参数`，但是顺序必须是：必选参数、默认参数、可变参数、关键字参数
```python
def person(name,age=0,*friends,**other):
	print 'Hello,',name
	print 'Your age is ',age
	for friend in friends:
		print friend ,' is your friend'
	print other

person('zhai',23,'joy','nike','jaky',city='beijing')
```
##递归函数
```python
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print fact(5)
```
尾递归
```python
def fact(n):
	return fact_iter(1,1,n)

def fact_iter(product,count,max):
	if count > max:
		return product
	return fact_iter(product*count,count+1,max)

print fact(888)
```