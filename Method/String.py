# Python String Methods with Explanation & Examples 

# 1. capitalize()
# Pehla letter capital kar deta hai aur baaki sab lower case me hota hai.


# text = "hello world"
# print(text.capitalize())  # Output: Hello world
# 2. casefold()
# Puri string ko lower case me convert kar deta hai (lower() se bhi zyada powerful).


# text = "HELLO WORLD"
# print(text.casefold())  # Output: hello world
# 3. center(width, char)
# String ko beech me center karta hai aur baaki jagah char se fill karta hai.


# text = "hi"
# print(text.center(10, '-'))  # Output: ----hi----
# 4. count(substring)
# Substring kitni baar aayi hai count karta hai.


# text = "banana"
# print(text.count("a"))  # Output: 3
# 5. encode()
# String ko bytes me convert karta hai.


# text = "hello"
# print(text.encode())  # Output: b'hello'
# 6. endswith(suffix)
# Check karta hai ke string ka end kisi specific text se ho raha hai ya nahi.


# text = "test.py"
# print(text.endswith(".py"))  # Output: True
# 7. expandtabs(tabsize)
# \t ko spaces me replace karta hai.


# text = "1\t2"
# print(text.expandtabs(4))  # Output: 1   2
# 8. find(substring)
# Substring ka index return karta hai, agar na ho to -1 deta hai.


# print("hello".find("e"))  # Output: 1
# 9. format()
# String me variables insert karne ke liye use hota hai.


# name = "Aman"
# print("My name is {}".format(name))  # Output: My name is Aman
# 10. format_map(mapping)
# Dictionary se values leke string me dalta hai.


# print("{x} {y}".format_map({'x':10, 'y':20}))  # Output: 10 20
# 11. index(substring)
# Substring ka index return karta hai, agar na ho to error deta hai.


# print("hello".index("e"))  # Output: 1
# 12. isalnum()
# Check karta hai string sirf alphabets aur numbers hai ya nahi.


# print("abc123".isalnum())  # Output: True
# 13. isalpha()
# Check karta hai string sirf alphabets hai ya nahi.


# print("abc".isalpha())  # Output: True
# 14. isascii()
# Check karta hai string sirf ASCII characters hai ya nahi.


# print("abc".isascii())  # Output: True
# 15. isdecimal()
# Check karta hai string sirf decimal digits hai ya nahi.


# print("123".isdecimal())  # Output: True
# 16. isdigit()
# Check karta hai string sirf digits hai ya nahi (superscripts bhi count hote hain).


# print("123".isdigit())  # Output: True
# 17. isidentifier()
# Check karta hai ke string valid Python variable name hai ya nahi.


# print("var1".isidentifier())  # Output: True
# 18. islower()
# Check karta hai string ke saare letters lower case hai ya nahi.


# print("abc".islower())  # Output: True
# 19. isnumeric()
# Check karta hai string sirf numeric characters hai ya nahi.


# print("123".isnumeric())  # Output: True
# 20. isprintable()
# Check karta hai string ke saare characters printable hai ya nahi.


# print("Hello!".isprintable())  # Output: True
# 21. isspace()
# Check karta hai string sirf spaces pe hai ya nahi.


# print("   ".isspace())  # Output: True
# 22. istitle()
# Check karta hai har word ka pehla letter capital hai ya nahi.


# print("Hello World".istitle())  # Output: True
# 23. isupper()
# Check karta hai string ke saare letters upper case hai ya nahi.


# print("ABC".isupper())  # Output: True
# 24. join(iterable)
# List ya tuple ke elements ko ek string me join karta hai.


# print("-".join(["a", "b", "c"]))  # Output: a-b-c
# 25. ljust(width, char)
# String ko left me rakhta hai aur baaki jagah char fill karta hai.


# print("hi".ljust(5, '-'))  # Output: hi---
# 26. lower()
# String ko lower case me convert karta hai.


# print("HELLO".lower())  # Output: hello
# 27. lstrip(chars)
# Start se spaces ya given chars remove karta hai.


# print("   hi".lstrip())  # Output: 'hi'
# 28. maketrans() & translate()
# Character replace karne ke liye map banata hai aur translate karta hai.


# trans = str.maketrans("abc", "123")
# print("abc".translate(trans))  # Output: 123
# 29. partition(sep)
# String ko 3 parts me divide karta hai.


# print("hello world".partition(" "))  
# # Output: ('hello', ' ', 'world')
# 30. removeprefix(prefix)
# String ke start se prefix remove karta hai.


# print("HelloWorld".removeprefix("Hello"))  # Output: World
# 31. removesuffix(suffix)
# String ke end se suffix remove karta hai.


# print("HelloWorld".removesuffix("World"))  # Output: Hello
# 32. replace(old, new)
# Substring ko replace karta hai.


# print("hi hi".replace("hi", "hello"))  # Output: hello hello
# 33. rfind(substring)
# Substring ka last occurrence ka index deta hai.


# print("hello".rfind("l"))  # Output: 3
# 34. rindex(substring)
# Substring ka last index deta hai, na ho to error deta hai.


# print("hello".rindex("l"))  # Output: 3
# 35. rjust(width, char)
# String ko right me rakhta hai aur baaki jagah char fill karta hai.


# print("hi".rjust(5, '-'))  # Output: ---hi
# 36. rpartition(sep)
# String ko right side se 3 parts me divide karta hai.


# print("hello world".rpartition(" "))  
# # Output: ('hello', ' ', 'world')
# 37. rsplit(sep, maxsplit)
# String ko right side se split karta hai.


# print("a,b,c".rsplit(",", 1))  # Output: ['a', 'b,c']
# 38. rstrip(chars)
# End se spaces ya chars remove karta hai.


# print("hi   ".rstrip())  # Output: 'hi'
# 39. split(sep)
# String ko list me split karta hai.


# print("a b c".split())  # Output: ['a', 'b', 'c']
# 40. splitlines()
# String ko lines me split karta hai.


# print("a\nb\nc".splitlines())  # Output: ['a', 'b', 'c']
# 41. startswith(prefix)
# Check karta hai string ka start kisi given text se ho raha hai ya nahi.


# print("hello".startswith("he"))  # Output: True
# 42. strip(chars)
# Start aur end se spaces ya chars remove karta hai.


# print("  hi  ".strip())  # Output: 'hi'
# 43. swapcase()
# Upper case ko lower aur lower ko upper me convert karta hai.


# print("HeLLo".swapcase())  # Output: hEllO
# 44. title()
# Har word ka pehla letter capital karta hai.


# print("hello world".title())  # Output: Hello World
# 45. upper()
# String ko upper case me convert karta hai.


# print("hi".upper())  # Output: HI
# 46. zfill(width)
# String ke start me zeros fill karta hai.


# print("42".zfill(5))  # Output: 00042