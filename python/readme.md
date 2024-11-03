
setup
conda create --name karl python=3.11.4

##  Read a file

```python
try:
    with open(filename, 'r') as f:
      data = f.read()
    except FileNotFoundError:
            print(f"Error, {filename} does not exist")


## all about strings
https://docs.python.org/3/library/string.html

```


```python
>>> s=" 123 \n"
>>> s
' 123 \n'
>>> s.strip()
'123'
>>> s.lstrip()
'123 \n'
>>> s.rstrip()
' 123'
>>> s.index('2')
2
>>> s.index('4')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> s =" a b a "
>>> s.replace('b', 'a')
' a a a '
>>> s.replace('a', 'b')
' b b b '

>>> s
' a b a '
>>> s.find('c')
-1
>>> s="a b c"
>>> s.split()
['a', 'b', 'c']
>>> s.split('b')
['a ', ' c']
>>> "b".join((s.split('b')))
'a b c'
>>> s=r'File=c:\temp\tmp{010}.txt'
>>> name,delim,value=s.partition('=')
>>> value
'c:\\temp\\tmp{010}.txt'

>>> "Abc124".isdigit()
False
>>> "12".isdigit()
True
>>> "-12".isdigit()
False
>>> "Abc".isalpha()
True
>>> "Abc124".isalnum()
True

>>> "a".islower()
True
>>> "A".isupper()
True

>>> "1".isnumeric()
True
>>> "-1".isnumeric()
False
>>> "12.5".isnumeric()
False
>>>


# Regex
# regex to matmch simple c# assignment with comment following
# variable can't start with number , but otherwise a word \w that includes underscores

>>> re.fullmatch("\s*([^0-9]*\w*)=\d+\s*;\s+//[a-z ]+",      'x=123;   // line of csharp code')
<re.Match object; span=(0, 31), match='x=123;   // line of csharp code'>

>>> re.sub(";", ' ','x_=123;')  # convert to python assignment
'x_=123 '
>>> re.split('[,\t\s]+',"x64\t,x86, \twin32")
['x64', 'x86', 'win32']

>>> re.search('\twin32',"x64\t,x86, \twin32")
<re.Match object; span=(10, 16), match='\twin32'>

>>> x = re.search('\twin32',"x64\t,x86, \twin32")
>>> if not x is None:
...     print(x.group())
...
        win32

>>> re.findall('\t?(\w+)',"x64\t,x86, \twin32")
['x64', 'x86', 'win32']

```
formatting and alignment of strings

https://docs.python.org/3/library/string.html#formatspec
```python
>>> s
' a b a '
>>> f"{s:^20}"
'       a b a        '
#01234567890123456789
```

```python
>>> s="Snake River"
>>> s[:4]
'Snak'
>>> s[:-1]
'Snake Rive'
s[::2]
'SaeRvr'

s[::1]
​'Snake River'
s[::5]
'S r'

>>> "Snake" in s
True

>>> s.split()
['Snake', 'River']

>>> s.upper()
'SNAKE RIVER'
>>> s.lower()
'snake river'
>>> s.title()
'Snake River'
>>> s.upper().isupper()
True
>>> s.startswith("Sn")
True
>>> s.endswith("er")
True

>>> i = 65
>>> print(f"{i:c}")
A
>>> x=12.456
>>> print(f"`{x:>22}`")
`                12.456`
>>> print(f"`{x:<22}`")
`12.456                `
>>> print(f"`{x:^22}`")
`        12.456        `
>>> x=1234567.89
>>> print(f"`{x:<15,.3f}`")
`1,234,567.890  ` 

```

## Exceptions

```python
try:
    num=12
    result = num/0
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print(f"result = {result}")
finally:
    print("let's cleanup here.")

#can't divide by zero
#let's cleanup here.
```

https://automatetheboringstuff.com/2e/chapter3/


ZeroDivisionError 

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
>>> a =[1,0,-1, -2, -3]
>>> a = a +[-4]
>>> a
[1, 0, -1, -2, -3, -4]
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

>>> x =list(range(1,5))
>>> x
[1, 2, 3, 4]
# create indexes to iterate backwards
>>> y =list(range(len(x)-1,-1,-1))
>>> y
[3, 2, 1, 0]
>>>

```
## random

```
import random
for i in range(10):
    print(random.random())  # value from zero (0) to 0.99999999999999.....

>>> random.random()
0.9829738732551279
```

https://docs.python.org/3/library/random.html#random.random

random.randrange(stop)  # integers
random.randrange(start, stop[, step])  # integers


## math

https://docs.python.org/3/library/math.html#module-math

## statistics
```
import statistics as stats
numbers = [1,1,1,1,1,1,88]
print(f"median = {stats.median(numbers)}")
print(f"average ={stats.mean(numbers)}")
```

## write to a file

```python

try:
    with open("{010}.txt","w") as f1:
        f1.write("a\n")
        f1.write("b\n")
except Exception:
    print("Something went off track, oops")
```

## numpy

https://numpy.org/doc/stable/user/whatisnumpy.html
https://numpy.org/doc/stable/user/quickstart.html


```python
>>> import numpy as np
>>> a = np.arange(1,11)
>>> a
array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
>>> m = np.arange(1,11).reshape(5,2)
>>> m
array([[ 1,  2],
       [ 3,  4],
       [ 5,  6],
       [ 7,  8],
       [ 9, 10]])
>>> m[2][1]
np.int64(6)
>>> m2 = m * 1.1
>>> m2
array([[ 1.1,  2.2],
       [ 3.3,  4.4],
       [ 5.5,  6.6],
       [ 7.7,  8.8],
       [ 9.9, 11. ]])
>>> m2[2][1]
np.float64(6.6000000000000005)
>>> m2[0]
array([1.1, 2.2])
>>> m2[1:3]
array([[3.3, 4.4],
       [5.5, 6.6]])
>>> m2[:,1] # get second column
array([ 2.2,  4.4,  6.6,  8.8, 11. ])
>>> m2[2:4,:]   # grab subset row 2,3 and  all columns
array([[5.5, 6.6],
       [7.7, 8.8]])

# attributes: https://numpy.org/doc/stable/user/absolute_beginners.html#array-attributes
>>> a = np.arange(1000)
>>> len(a)
1000
>>> a.ndim
1
>>> a.size
1000
>>> a.shape
(1000,)
>>> a.dtype
dtype('int64')
>>>
>>> a.sum()
np.int64(499500)
>>> a.max()
np.int64(999)


```


## Pandas

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html


https://pandas.pydata.org/pandas-docs/stable/reference/frame.html

class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)


```python
import pandas as pd
from datetime import datetime


def t(str) -> datetime:
    return datetime.strptime(str, '%Y-%m-%d')

flow_series = pd.Series([300, 350., 298., 450],
                        index=[t('2024-01-01'), t('2024-01-02'), t('2024-01-03'), t('2024-01-04')])


print(flow_series)
# 2024-01-01    300.0
# 2024-01-02    350.0
# 2024-01-03    298.0
# 2024-01-04    450.0
# dtype: float64

mydf = pd.read_csv("nice_file.csv")

```


##  TextBlob

https://textblob.readthedocs.io/en/stable/quickstart.html#quickstart
setup

```bat
pip install textblob
python -m textblob.download_corpora

```python

>>> from textblob import TextBlob
>>> tb = TextBlob("Python 3.12.4  packaged by Anaconda, Inc. (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32")
>>> tb.sentiment
Sentiment(polarity=0.16666666666666666, subjectivity=0.3333333333333333)
>>> import nltk
>>> nltk.download('punkt_tab')
>>> tb.sentences
[Sentence("Python 3.12.4  packaged by Anaconda, Inc. (main, Jun 18 2024, 15:03:56) [MSC v.1929 64 bit (AMD64)] on win32")]
>>> tb.sentences

>>> tb.words
WordList(['Python', '3.12.4', 'packaged', 'by', 'Anaconda', 'Inc', 'Another', 'sentance', 'here', 'main', 'Jun', '18', '2024', '15:03:56', 'MSC', 'v.1929', '64', 'bit', 'AMD64', 'on', 'win32'])
>>> 
>>> tb.noun_phrases
WordList(['python', 'jun', 'msc', 'amd64'])
>>> tb.tags
[('Python', 'NNP'), ('3.12.4', 'CD'), ('packaged', 'VBN'), ('by', 'IN'), ('Anaconda', 'NNP'), ('Inc.', 'NNP'), ('main', 'JJ'), ('Jun', 'NNP'), ('18', 'CD'), ('2024', 'CD'), ('15:03:56', 'CD'), ('[', 'NN'), ('MSC', 'NNP'), ('v.1929', 'VBZ'), ('64', 'CD'), ('bit', 'NN'), ('AMD64', 'NNP'), (']', 'VBP'), ('on', 'IN'), ('win32', 'NN')]


```
# TextBlob spell checking examples

```python
>>> from textblob import TextBlob
>>> txt = "I cann't spellll vwery wwell"
>>> tb = TextBlob(txt)
>>> tb.correct()
TextBlob("I can't spell very well")
>>> from textblob import Word
>>> for word in txt.split():
...     o = Word(word)
...     print(o.spellcheck())
...
[('I', 1.0)]
[('cannot', 1.0)]
[('spell', 0.8181818181818182), ('spells', 0.09090909090909091), ('spelled', 0.09090909090909091)]
[('very', 1.0)]
[('well', 0.9892650701899257), ('dwell', 0.006606110652353427), ('swell', 0.004128819157720892)]
>>>

```

# style guide

https://peps.python.org/pep-0000/   

## Resoures:


https://automatetheboringstuff.com/2e/

udemy.com  100-days-of-code

http://reeborg.ca/reeborg.html


https://html5up.net/
