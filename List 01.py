Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[8,1.2,True,12j,"Hello"]

a[0]
8
a[4][0]
'H'
len(a)
5
id(a)
1923339663872
id(a[1])
1923334453936
a[4][1]
'e'
a[4][4]
'o'
bool(a)
True
>>> list()
[]
>>> 
>>> a
[8, 1.2, True, 12j, 'Hello']
>>> a.append(False)
>>> a
[8, 1.2, True, 12j, 'Hello', False]
>>> # syntax for append is   var_name.append(Value)
>>> a.extend([99,"Qspider","Pune"])
>>> a
[8, 1.2, True, 12j, 'Hello', False, 99, 'Qspider', 'Pune']
>>> # syntax :- var_name.extend([val1,val2,val3,.....])
>>> # insert    syntax:- var_name.insert(index,value)
>>> a.insett(0,"Bhushan")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.insett(0,"Bhushan")
AttributeError: 'list' object has no attribute 'insett'. Did you mean: 'insert'?
>>> a.insert(0,"Bhushan")
... 
>>> a
['Bhushan', 8, 1.2, True, 12j, 'Hello', False, 99, 'Qspider', 'Pune']
>>> # deleting values
>>> a
['Bhushan', 8, 1.2, True, 12j, 'Hello', False, 99, 'Qspider', 'Pune']
>>> a.pop()
'Pune'
>>> a
['Bhushan', 8, 1.2, True, 12j, 'Hello', False, 99, 'Qspider']
>>> a.remove("Qspider")
>>> a
['Bhushan', 8, 1.2, True, 12j, 'Hello', False, 99]
>>> # replacing the values
>>> a[1]="data science"
>>> a
['Bhushan', 'data science', 1.2, True, 12j, 'Hello', False, 99]
>>> b=[23,"hi"]
>>> a.extent(b)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a.extent(b)
AttributeError: 'list' object has no attribute 'extent'. Did you mean: 'extend'?
>>> a(extend(b))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a(extend(b))
NameError: name 'extend' is not defined
>>> a.extend(b)
>>> a
['Bhushan', 'data science', 1.2, True, 12j, 'Hello', False, 99, 23, 'hi']
