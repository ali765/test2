#!/usr/bin/env/ python
print("hello")

my_name = input("please enter \n your name ")

print("hi " + my_name)

a = 7;

print('a')

print(my_name[0])

print(my_name.upper())

test_1 = "ali sater restom "

print(test_1.split())

print("the {0} {1} {2} {3}".format('a', 'b', 'c', 'd'))

res = 100 / 777

print("the result was: {r:1.3f}".format(r=res))
name = "Sam"
age = 3
print(f'{name} is {age} year old.')
d = {'key1': ['a', 'b', 'c']}
myl = d['key1']
print("{r}".format(r=myl))
letter = myl[2]
print("{s}".format(s=letter))
d = {'k1': 100, 'k2': 200}
print(d)
d['k3'] = 300
print(d)
d['k1'] = 'NEW VALUE'
print(d)
print(d.keys())
print(d.values())
print(d.items())
t = (1, 2, 3)
myl = [1, 2, 3]
print(type(t))
print(type(myl))

t = ('a', 'a', 'a', 'b')
print(t.count('a'))
print(t.index('a'))
print(t.count('b'))
