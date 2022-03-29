


# some regex used in intellij

```regex
@scriptable
@scriptable\s*\*/\s*@Scriptable
@scriptable\s*\*/\s*public


import hec.lang.annotation.Scriptable;


--- code that allready has upgraded, remove @scriptable.
find:
@scriptable(\s*\*/\s*@Scriptable)
replace:
$1

-- find duplicate Scriptable
find:
@Scriptable\s*@Scriptable

--- insert scriptable
find:
@scriptable(\s*\*/\n)
replace:
$1\t@Scriptable\n

@Scriptable(\s*\*/\n)

some code needs two \n\n to tab properly..
