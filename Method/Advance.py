# ********************************Python Bool Methods (3)**********************************#

b1 = True

# 1. __and__()
print("1. b1 & False:", b1 & False)
#  Boolean AND operation karta hai
# Output: False

# 2. __or__()
print("2. b1 | False:", b1 | False)
#  Boolean OR operation karta hai
# Output: True

# 3. __invert__()
print("3. ~b1:", ~b1)
#  Boolean NOT operation ke jaisa (bitwise)
# Output: -2

# ********************************Python Function Methods (10)**********************************#
def my_func(a,b):
    return a+b

# 1. __call__()
print("1. my_func(2,3):", my_func(2,3))
#  Function ko call karta hai
# Output: 5

# 2. __name__
print("2. my_func.__name__:", my_func.__name__)
#  Function ka name return karta hai
# Output: 'my_func'

# 3. __doc__
print("3. my_func.__doc__:", my_func.__doc__)
#  Function ka documentation string return karta hai
# Output: None (agar define nahi kiya)

# 4. __annotations__
print("4. my_func.__annotations__:", my_func.__annotations__)
#  Function arguments aur return ke type hints
# Output: {}

# 5. __defaults__
print("5. my_func.__defaults__:", my_func.__defaults__)
#  Function ke default argument values
# Output: None

# 6. __code__
print("6. my_func.__code__:", my_func.__code__)
#  Function ke bytecode aur metadata
# Output: <code object my_func at ...>

# 7. __globals__
print("7. my_func.__globals__:", list(my_func.__globals__.keys())[:5])
#  Function ke global namespace
# Output: ['__name__','__doc__','__package__',...]

# 8. __closure__
print("8. my_func.__closure__:", my_func.__closure__)
#  Free variables closure return karta hai
# Output: None

# 9. __kwdefaults__
print("9. my_func.__kwdefaults__:", my_func.__kwdefaults__)
#  Keyword-only default arguments
# Output: None

# 10. __dict__
print("10. my_func.__dict__:", my_func.__dict__)
#  Function attributes dictionary
# Output: {}

# ********************************Python Module Methods (5)**********************************#

import math

# 1. dir()
print("1. dir(math)[:5]:", dir(math)[:5])
#  Module ke attributes aur methods list karta hai
# Output: ['__doc__', '__loader__', '__name__', '__package__', '__spec__']

# 2. getattr()
print("2. getattr(math,'pi'):", getattr(math,'pi'))
#  Module attribute get karta hai
# Output: 3.141592653589793

# 3. hasattr()
print("3. hasattr(math,'sqrt'):", hasattr(math,'sqrt'))
#  Check karta hai attribute exist karta hai ya nahi
# Output: True

# 4. __name__
print("4. math.__name__:", math.__name__)
#  Module ka name return karta hai
# Output: 'math'

# 5. __doc__
print("5. math.__doc__:", math.__doc__[:50])
#  Module ka documentation
# Output: 'This module provides access to the mathematical functions...'

# ********************************Python File Methods (10)**********************************#

# 1. open()
f = open("test.txt","w")
print("1. open('test.txt','w'):", f)
#  File open karta hai
# Output: <_io.TextIOWrapper ...>

# 2. write()
f.write("Hello Siddiqui")
print("2. f.write('Hello Siddiqui')")
#  File me text write karta hai
# Output: 13 (number of characters written)

# 3. read()
f.close()
f = open("test.txt","r")
print("3. f.read():", f.read())
#  File ka content read karta hai
# Output: 'Hello Siddiqui'

# 4. readline()
f = open("test.txt","r")
print("4. f.readline():", f.readline())
#  File ka ek line read karta hai
# Output: 'Hello Siddiqui'

# 5. readlines()
print("5. f.readlines():", f.readlines())
#  File ke saare lines list me return karta hai
# Output: []

# 6. close()
f.close()
print("6. f.close() called")
#  File close karta hai

# 7. flush()
f = open("test.txt","w")
f.write("Siddiqui")
f.flush()
print("7. f.flush() called")
#  Buffer ko write karta hai file me

# 8. seek()
f.seek(0)
print("8. f.seek(0) called")
#  File pointer set karta hai

# 9. tell()
print("9. f.tell():", f.tell())
#  Current file pointer ka position
# Output: 0

# 10. fileno()
print("10. f.fileno():", f.fileno())
#  OS level file descriptor return karta hai
# Output: 3 (example)
f.close()

# ********************************Python Regex Methods (7)**********************************#

import re
pattern = re.compile(r'\d+')
text = "My number is 12345"

# 1. match()
print("1. pattern.match(text):", pattern.match(text))
#  String ke start se match karta hai, agar nahi to None
# Output: None

# 2. search()
print("2. pattern.search(text):", pattern.search(text))
#  String me first match dhundta hai
# Output: <re.Match object; span=(13,18), match='12345'>

# 3. findall()
print("3. pattern.findall(text):", pattern.findall(text))
#  Sab matches list me return karta hai
# Output: ['12345']

# 4. finditer()
print("4. list(pattern.finditer(text)):", list(pattern.finditer(text)))
#  Sab matches iterator return karta hai
# Output: [<re.Match object; span=(13,18), match='12345'>]

# 5. split()
print("5. re.split(r' ',text):", re.split(r' ',text))
#  String ko pattern ke basis pe split karta hai
# Output: ['My','number','is','12345']

# 6. sub()
print("6. re.sub(r'\d+','NUM',text):", re.sub(r'\d+','NUM',text))
#  Pattern ko replace karta hai
# Output: 'My number is NUM'

# 7. fullmatch()
print("7. pattern.fullmatch('12345'):", pattern.fullmatch("12345"))
#  Pure string match karta hai
# Output: <re.Match object; span=(0,5), match='12345'>


# ********************************Python Bytes / Bytearray Methods (15+)**********************************#

b = b'hello'

# 1. capitalize()
print("1. b.capitalize():", b.capitalize())
#  Pehla letter uppercase kare aur baaki lowercase
# Output: b'Hello'

# 2. center()
print("2. b.center(10,b'-'):", b.center(10,b'-'))
#  Bytes ko center me rakhta hai aur fill char se fill
# Output: b'---hello--'

# 3. count()
print("3. b.count(b'l'):", b.count(b'l'))
#  Byte element kitni baar hai count
# Output: 2

# 4. decode()
print("4. b.decode():", b.decode())
#  Bytes ko string me convert
# Output: 'hello'

# 5. endswith()
print("5. b.endswith(b'o'):", b.endswith(b'o'))
#  Check karta hai suffix
# Output: True

# 6. find()
print("6. b.find(b'l'):", b.find(b'l'))
#  Index of first occurrence
# Output: 2

# 7. index()
print("7. b.index(b'l'):", b.index(b'l'))
#  Index of first occurrence
# Output: 2

# 8. isalnum()
print("8. b.isalnum():", b.isalnum())
#  Check letters/digits
# Output: True

# 9. isalpha()
print("9. b.isalpha():", b.isalpha())
#  Check letters only
# Output: True

# 10. isdigit()
print("10. b.isdigit():", b.isdigit())
#  Check digits only
# Output: False

# 11. lower()
print("11. b.lower():", b.lower())
#  Lowercase bytes
# Output: b'hello'

# 12. replace()
print("12. b.replace(b'l',b'L'):", b.replace(b'l',b'L'))
#  Replace bytes
# Output: b'heLLo'

# 13. split()
print("13. b.split(b'l'):", b.split(b'l'))
#  Split bytes
# Output: [b'he',b'','o']

# 14. strip()
b2 = b'  hello  '
print("14. b2.strip():", b2.strip())
#  Leading/trailing spaces remove
# Output: b'hello'

# 15. upper()
print("15. b.upper():", b.upper())
#  Uppercase bytes
# Output: b'HELLO'
