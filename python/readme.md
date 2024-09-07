

## Indexing and slices.

```python
>>> a = [1,2,3,4,5]
>>> a[0:-1]
[1, 2, 3, 4]
>>> a[:]
[1, 2, 3, 4, 5]
>>> a[-1]
5
>>> a[:-1]
[1, 2, 3, 4]
>>> a = a + [6]
>>> a
[1, 2, 3, 4, 5, 6]
>>> del a[5]
>>> a
[1, 2, 3, 4, 5]
>>> a.remove(1)
>>> a
[2, 3, 4, 5]

>>> a
[10, 20, 30, 40]
>>> a[0:1] = [1,2]
>>> a
[1, 2, 20, 30, 40]

```
##  List:   insert, extend, remove, clear , count, copy, sum, len
```python

>> a=[-1,-2,-3]
>>> a.insert(0,0)
>>> a.insert(0,1)
>>> a
[1, 0, -1, -2, -3]

>>> a.extend([-5,-6])
>>> a
[1, 0, -1, -2, -3, -4, -5, -6]
>>> a.remove(-2)
>>> a
[1, 0, -1, -3, -4, -5, -6]

>>> a.clear()
>>> a
[]
>>> a
[5, 5, 6, 6, 7, 8]
>>> a.count(6)
2
>>> a.reverse()
>>> a
[8, 7, 6, 6, 5, 5]

>>> b = a.copy()
>>> b
[8, 7, 6, 6, 5, 5]
>>> sum(b)
37
>>> len(b)
6
```

## append to list

```python
>>> count =[]
>>> for num in range(0,10):
...     count += [num]
...
>>> count
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> count += [10,11,12]
>>> count
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = a+b
>>> c
[1, 2, 3, 4, 5, 6]

>>> a
[1, 2, 3, 4, 5, 6]
>>> a.append(7)
>>> a
[1, 2, 3, 4, 5, 6, 7]



```

## compare lists
```python

>>> a=[1,2,4]
>>> b =[1,2,4]
>>> a == b
True
>>> b =[1,2,3]
>>> a == b
False
```


## sort a list

```python

>> a = [3,6,1,12,-1,0]
>>> a.sort()
>>> a
[-1, 0, 1, 3, 6, 12]
>>> a = [3,6,1,12,-1,0]
>>> b = sorted(a)
>>> b
[-1, 0, 1, 3, 6, 12]
```

## searching in List
```python
>>> a=[5,6,7]
>>> a.index(6)
1
>>> a.index(6,1)
1
>>> a.index(6,1,4)
1
>>> has_6 = 6 in a
>>> has_6
True
```

# Dictionary: get, in, values, keys
```python
>>> d = { 1 : 'x', 2 : 'y'}
>>> 'x' in d
False
>>> 1 in d
True
>>> 'x' in d.values()
True
>>> print(d.get(5))
None
>>> print(d.get(5,'empty'))
empty
>>> print(d.get(1,'empty'))
x
>>> d[1]
'x'

{'Boise River': 1200, 'Snake River': 2500}
>>> flows['Payette River']= 5000
>>> flows
{'Boise River': 1200, 'Snake River': 2500, 'Payette River': 5000}
>>> del flows['Boise River']
>>> flows
{'Snake River': 2500, 'Payette River': 5000}
>>>
>>> for river in flows:
...     print(river)
...
Snake River
Payette River
>>> for river in flows.keys():
...     print(river)
...
Snake River
Payette River

>>> for river in flows.items():
...     print(river)
...
('Snake River', 2500)
('Payette River', 5000)

>>> flows.keys()
dict_keys(['Snake River', 'Payette River'])
>>> a = list(flows.keys())
>>> a
['Snake River', 'Payette River']
>>> a = sorted(flows.keys())
>>> a
['Payette River', 'Snake River']

>>> len(flows)
2

see also:
https://automatetheboringstuff.com/2e/chapter5/
for example on counting characters
dict.setdefault(key,default_value)
dict[key] += dict[key] +1
```

# Tuple is immuatable 
```python
>>> t =(1,2,3)
>>> id(t)
1928833554816
>>> t = t + (4,5)
>>> t
(1, 2, 3, 4, 5)
>>> id(t)
1928802889872
```

## looping

```
flows = [100, 500, 600, 1700 ,3456]
x = []
for f in flows:
    x.append(f)

for i in range(1 ,3):
    x.append(i)

print(x)
# [100, 500, 600, 1700, 3456, 1, 2]

#function
def func1(a):
    try:
        print(f"a={a}")
    except NotImplementedError:
        print('error')

func1(12)
print("Karl " ,end='')
print(" T.")
#a=12
#Karl  T
```
## random

```
import random
for i in range(10):
    print(random.random())

```

## statistics
```
import statistics as stats
numbers = [1,1,1,1,1,1,88]
print(f"median = {stats.median(numbers)}")
print(f"average ={stats.mean(numbers)}")
```


# style guide

https://peps.python.org/pep-0000/   

## Resoures:


https://automatetheboringstuff.com/2e/

udemy.com  100-days-of-code

http://reeborg.ca/reeborg.html


https://html5up.net/
