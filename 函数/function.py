# !/usr/bin/env python
# -*- coding:utf-8 -*-

abs(-100) # 求绝对值
int('123')	#类型转换
float('1.23')
unicode(123)
bool(1)
bool('')

# 函数定义
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print my_abs(-1)

# 空函数
def nop():
	pass

# 参数检查
def my_abs(x):
	if not ininstance(x,(int,float)): 	# ininstance作参数类型检查
		raise TypeError('bad operand type') 
	if x >= 0:
		return x
	else:
		return -x

import math

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

x,y = move(100,100,60,math.pi / 6)
n,m = move(100,100,20)
print x,y
print n,m

#可变参数
def calc(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum

print calc([1,2,3])

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print calc(1,2,3,4)
print calc()


def person(name,age=0,*friends,**other):
	print 'Hello,',name
	print 'Your age is ',age
	for friend in friends:
		print friend ,' is your friend'
	print other

person('zhai',23,'joy','nike','jaky',city='beijing')

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print fact(5)

def fact(n):
	return fact_iter(1,1,n)

def fact_iter(product,count,max):
	if count > max:
		return product
	return fact_iter(product*count,count+1,max)

print fact(888)