# ********************************Python List Methods (12)**********************************#

# 1. append()
lst1 = [1,2,3]
lst1.append(4)
print("1. lst1.append(4):", lst1)
#  List ke end me element add karta hai
# Output: [1, 2, 3, 4]

# 2. extend()
lst2 = [1,2]
lst2.extend([3,4])
print("2. lst2.extend([3,4]):", lst2)
#  Multiple elements add karta hai list ke end me
# Output: [1, 2, 3, 4]

# 3. insert()
lst3 = [1,2,3]
lst3.insert(1,100)
print("3. lst3.insert(1,100):", lst3)
#  Index 1 pe element add karta hai
# Output: [1, 100, 2, 3]

# 4. remove()
lst4 = [1,2,100,3]
lst4.remove(100)
print("4. lst4.remove(100):", lst4)
#  First occurrence of element remove karta hai
# Output: [1,2,3]

# 5. pop()
lst5 = [1,2,3,4]
val = lst5.pop(2)
print("5. lst5.pop(2):", val, lst5)
#  Index 2 ka element remove karta hai aur return karta hai
# Output: 3 [1,2,4]

# 6. clear()
lst6 = [1,2,3]
lst6.clear()
print("6. lst6.clear():", lst6)
#  Sab elements remove karta hai
# Output: []

# 7. index()
lst7 = [1,2,3,2]
print("7. lst7.index(2):", lst7.index(2))
#  Element ka first index return karta hai
# Output: 1

# 8. count()
lst8 = [1,2,2,3]
print("8. lst8.count(2):", lst8.count(2))
#  Element kitni baar appear hota hai count karta hai
# Output: 2

# 9. sort()
lst9 = [3,1,2]
lst9.sort()
print("9. lst9.sort():", lst9)
#  List ko ascending order me sort karta hai
# Output: [1,2,3]

# 10. reverse()
lst10 = [1,2,3]
lst10.reverse()
print("10. lst10.reverse():", lst10)
#  List ka order ulta kar deta hai
# Output: [3,2,1]

# 11. copy()
lst11 = [1,2,3]
new_lst11 = lst11.copy()
print("11. new_lst11 = lst11.copy():", new_lst11)
#  List ka shallow copy return karta hai
# Output: [1,2,3]

# 12. + operator / * operator
lst12 = [1,2]
print("12. lst12 + [3,4]:", lst12 + [3,4])
print("12. lst12 * 2:", lst12*2)
#  Concatenate ya repeat karta hai list ko
# Output: [1,2,3,4]
#         [1,2,1,2]

# ********************************Python Tuple Methods (2)**********************************#

tpl1 = (1,2,3,2)

# 1. count()
print("1. tpl1.count(2):", tpl1.count(2))
#  Element kitni baar appear hota hai count karta hai
# Output: 2

# 2. index()
print("2. tpl1.index(3):", tpl1.index(3))
#  Element ka first index return karta hai
# Output: 2


# ********************************Python Set Methods (11)**********************************#

s1 = {1,2,3}

# 1. add()
s1.add(4)
print("1. s1.add(4):", s1)
#  Set me element add karta hai
# Output: {1,2,3,4}

# 2. remove()
s1.remove(2)
print("2. s1.remove(2):", s1)
#  Element remove karta hai, agar nahi ho to error
# Output: {1,3,4}

# 3. discard()
s1.discard(5)
print("3. s1.discard(5):", s1)
#  Element remove karta hai, agar nahi ho to error nahi
# Output: {1,3,4}

# 4. pop()
val = s1.pop()
print("4. s1.pop():", val, s1)
#  Random element remove aur return karta hai
# Output: 1 {3,4} (example)

# 5. clear()
s1.clear()
print("5. s1.clear():", s1)
#  Sab elements remove karta hai
# Output: set()

# 6. union()
s2 = {1,2}; s3 = {2,3}
print("6. s2.union(s3):", s2.union(s3))
#  Sets combine karta hai without duplicates
# Output: {1,2,3}

# 7. intersection()
print("7. s2 & s3:", s2 & s3)
#  Common elements return karta hai
# Output: {2}

# 8. difference()
print("8. s2 - s3:", s2 - s3)
#  Elements jo dusre set me nahi
# Output: {1}

# 9. symmetric_difference()
print("9. s2 ^ s3:", s2 ^ s3)
#  Jo sirf ek set me hai return karta hai
# Output: {1,3}

# 10. issubset()
print("10. {1}.issubset(s2):", {1}.issubset(s2))
#  Check karta hai agar subset hai ya nahi
# Output: True

# 11. issuperset()
print("11. s2.issuperset({1}):", s2.issuperset({1}))
#  Check karta hai agar superset hai ya nahi
# Output: True

# ********************************Python Dict Methods (15)**********************************#

d1 = {"a":1, "b":2}

# 1. get()
print("1. d1.get('a'):", d1.get('a'))
#  Key ka value return karta hai, agar nahi ho to None
# Output: 1

# 2. keys()
print("2. d1.keys():", list(d1.keys()))
#  Keys ka list return karta hai
# Output: ['a','b']

# 3. values()
print("3. d1.values():", list(d1.values()))
#  Values ka list return karta hai
# Output: [1,2]

# 4. items()
print("4. d1.items():", list(d1.items()))
#  (key,value) tuple return karta hai
# Output: [('a',1),('b',2)]

# 5. pop()
val = d1.pop('a')
print("5. d1.pop('a'):", val, d1)
#  Key-value remove karta hai aur value return karta hai
# Output: 1 {'b':2}

# 6. popitem()
item = d1.popitem()
print("6. d1.popitem():", item, d1)
#  Last inserted item remove aur return karta hai
# Output: ('b',2) {}

# 7. clear()
d1 = {"a":1,"b":2}
d1.clear()
print("7. d1.clear():", d1)
#  Sab remove karta hai
# Output: {}

# 8. update()
d1.update({"c":3})
print("8. d1.update({'c':3}):", d1)
#  Add ya update key-value
# Output: {'c':3}

# 9. setdefault()
val = d1.setdefault("d",4)
print("9. d1.setdefault('d',4):", val, d1)
#  Agar key nahi hai to add karta hai aur return karta hai
# Output: 4 {'c':3,'d':4}

# 10. copy()
new_d = d1.copy()
print("10. new_d = d1.copy():", new_d)
#  Shallow copy return karta hai
# Output: {'c':3,'d':4}

# 11. fromkeys()
keys = ["x","y"]
new_dict = dict.fromkeys(keys,0)
print("11. dict.fromkeys(['x','y'],0):", new_dict)
#  New dict create karta hai given keys aur default value
# Output: {'x':0,'y':0}

# 12. get() with default
print("12. d1.get('z',0):", d1.get("z",0))
#  Agar key nahi hai to default return karta hai
# Output: 0

# 13. pop() with default
print("13. d1.pop('z',0):", d1.pop("z",0))
#  Agar key nahi ho to default return
# Output: 0

# 14. len()
print("14. len(d1):", len(d1))
#  Dict me number of keys return karta hai
# Output: 2

# 15. 'in' operator
print("15. 'c' in d1:", 'c' in d1)
#  Check karta hai key exist karti hai ya nahi
# Output: True
