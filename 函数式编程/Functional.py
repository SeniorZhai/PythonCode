# -*- coding:utf-8 -*-

def f(x):
	print x*x

map(f,range(1,10))


def f(x,y):
	print y,x,"* 10"
	return y + x * 10
print reduce(f,[1,2,3]) 
