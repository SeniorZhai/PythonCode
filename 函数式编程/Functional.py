# -*- coding:utf-8 -*-

def f(x):
	print x*x

map(f,range(1,10))


def f(x,y):
	print y,x,"* 10"
	return y + x * 10
print reduce(f,[1,2,3]) 

l = [2,3,1,32,11,34,12]
print sorted(l)

def cmp(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	return 0

print sorted([2,3,1,32,11,34,12],cmp)