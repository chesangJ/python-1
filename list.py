s.index("a")
4
>>> s[0]
'A'
>>> s[1]
'k'
>>> s[3]
'r'
>>> s[6]
'h'
>>> s=[8]
>>> s
[8]
>>> s="Akirachix"
>>> s[8]
'x'
>>> s[9]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> s[-1]
'x'
>>> s[-5]
'a'
>>> s[-8]
'k'
>>> s[-9]
'A'
>>> s[0:3]
'Aki'
>>> s[1:4]
'kir'
>>> s[4:3]
''
>>> s[4:8]
'achi'
>>> S[3: ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'S' is not defined
>>> S[3: ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'S' is not defined
>>> s[3: ]
'rachix'
>>> s[-8:-6]
'ki'
>>> s[-5:-2]
'ach'
>>> s[-2: ]
'ix'
>>> s[-3:-7]
''
>>> s[-4: ]
'chix'
>>> s[-5:8]
'achi'
>>> s[3:-3]
'rac'
>>> s[-3:3]
''
>>> s[1:-3]
'kirac'
>>> s[-6:7]
'rach'
>>> s
'Akirachix'
>>> A
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined
>>> x=[1,2,3,4]
>>> y=["a,b,c,d"]
>>> z[true,"a",3,3.4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> z=[true,"a",3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> y
['a,b,c,d']
>>> z=["true","a",3]
>>> type x
  File "<stdin>", line 1
    type x
         ^
SyntaxError: invalid syntax
>>> type (x)
<class 'list'>
>>> type (y)
<class 'list'>
>>> a=[1,2,3,4]
>>> b=[5,6,7]
>>> c=a+b
>>> c
[1, 2, 3, 4, 5, 6, 7]
>>> d=a*3
>>> d
[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
>>> e=s*3
>>> e
'AkirachixAkirachixAkirachix'
>>> dir (a)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> fruits=["mango","apple","banana","passion","melon"]
>>> fruits.append ("pineapple")
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineapple']
>>> fruits.extend(["orange","grapes")
  File "<stdin>", line 1
    fruits.extend(["orange","grapes")
                                    ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> fruits.extend(["orange","grapes")
  File "<stdin>", line 1
    fruits.extend(["orange","grapes")
                                    ^
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> fruits.extend(["oranges","grapes"])
>>> fruits
['mango', 'apple', 'banana', 'passion', 'melon', 'pineapple', 'oranges', 'grapes']
>>> fruits.insert(1,avocado)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'avocado' is not defined
>>> fruits.insert(1,"avocado")
>>> fruits
['mango', 'avocado', 'apple', 'banana', 'passion', 'melon', 'pineapple', 'oranges', 'grapes']
>>> fruits.sort()
>>> fruits
['apple', 'avocado', 'banana', 'grapes', 'mango', 'melon', 'oranges', 'passion', 'pineapple']
>>> fruits.reverse()
>>> fruits
['pineapple', 'passion', 'oranges', 'melon', 'mango', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.remove("melon")
>>> fruits
['pineapple', 'passion', 'oranges', 'mango', 'grapes', 'banana', 'avocado', 'apple']
>>> fruits.pop()
'apple'
>>> fruits
['pineapple', 'passion', 'oranges', 'mango', 'grapes', 'banana', 'avocado']
>>> len(fruits)
7
>>> fruits[0]
'pineapple'
>>> fruits[3]
'mango'
>>> fruits[6]
'avocado'
>>> fruits[7]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> fruit[3:5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruit' is not defined
>>> fruits[ :4]
['pineapple', 'passion', 'oranges', 'mango']
>>> fruits[3:5]
['mango', 'grapes']
>>> fruits[2: ]
['oranges', 'mango', 'grapes', 'banana', 'avocado']
>>> x=[1,2,3,4,5]
>>> for n in x:print(n)
... 
1
2
3
4
5
>>> for n in x:print n*10
  File "<stdin>", line 1
    for n in x:print n*10
                     ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(n*10)?
>>> for n in x:print (n*10)
... 
10
20
30
40
50
>>> for n in x :print (n*n)
... 
1
4
9
16
25
>>> for z in fruits:print(z.upper)
... 
<built-in method upper of str object at 0x7f07ae513af0>
<built-in method upper of str object at 0x7f07ae5131b0>
<built-in method upper of str object at 0x7f07afd2ae70>
<built-in method upper of str object at 0x7f07ae513a70>
<built-in method upper of str object at 0x7f07af4ad5b0>
<built-in method upper of str object at 0x7f07ae513ab0>
<built-in method upper of str object at 0x7f07ae513c30>
>>> for z in fruits:print (z.upper())
... 
PINEAPPLE
PASSION
ORANGES
MANGO
GRAPES
BANANA
AVOCADO
>>> for fruit in fruits:print(fruit.capitalize())
... 
Pineapple
Passion
Oranges
Mango
Grapes
Banana
Avocado
>>> 
