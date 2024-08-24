

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
