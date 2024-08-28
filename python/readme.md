

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
