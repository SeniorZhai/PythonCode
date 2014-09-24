# !/usr/bin/env python
# -*- coding: utf-8 -*-
print 'begin>>>'
name = raw_input('please enter your name : ')
print 'hello,',name
print '''lin1
...line2
...line3'''

print '3>2',3>2
print '2<3',2<3
print '3>=3',3>=3

print 'True or False:',True or False
print 'True or True:',True or True
print 'False or False:',False or False

print 'True and False:',True and False
print 'False and False:',False and False
print 'True and True:',True and True

print 'not True',not True
print 'not False',not False

print 'None:',None

print ord('A')
print chr(65)

print u'中文'

print name.encode('utf-8')
print 'ABC'.encode('utf-8')	# 转换成utf-8

print u'\'中文\'的编码长度:',len(u'中文')

print 'abc'.decode('utf-8')		# 将字符串'xxx'转换成Unicode字符串u'xxx'
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

print 'Hi,%s,you have $%d' % (name,10000)	# %d整数 %f 浮点数 %s 字符串 %x 十六进制数

classmates = ['joy','bob','tracy']
print classmates
print len(classmates)
print classmates[2]
classmates.insert(1,name)
print classmates
classmates.append('end')
print classmates
classmates.pop()
print classmates
classmates.pop(1)
print classmates
L = ['Apple',1,[2,'2']]
print L
print len(L)
print L[2][1]

# tuple 不可变的list
classmates = ('a','b','c')
print classmates

t = (1,)
print t

age = 20
if age >= 18:
	print u'成年人'
else:
	print u'未成年人'

# 遍历
for name in classmates:
	print name

# 生成一个整数序列
print range(5)

# int()转换成整数
print int(raw_input("input number:"))

d = {'zoe':19,'joy':20,'jack':85}
print d

print d.get('thomas',-1)
d.pop('zoe')
print d

s = set([1,2,3])
print s
s.add(4)
print s
s.remove(2)
print s

a = ['1','d','10']
a.sort()
print a

a = 'abc'
print a.replace('a','A')