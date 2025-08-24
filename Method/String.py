#************************************Python String Methods**************************************#

# 1. capitalize()
str1 = "hello world"
print("1. str1.capitalize():", str1.capitalize())
# Roman: Pehla letter capital karta hai, baaki lowercase
# Output: "Hello world"

# 2. casefold()
str2 = "HELLO WORLD"
print("2. str2.casefold():", str2.casefold())
# Roman: String ko aggressive lowercase me convert karta hai
# Output: "hello world"

# 3. center(width, fillchar)
str3 = "Hello"
print("3. str3.center(10,'*'):", str3.center(10,'*'))
# Roman: String ko center karta hai aur extra space fillchar se fill karta hai
# Output: "**Hello***"

# 4. count(substring)
str4 = "hello hello world"
print("4. str4.count('hello'):", str4.count("hello"))
# Roman: Substring kitni baar hai count karta hai
# Output: 2

# 5. encode(encoding)
str5 = "Siddiqui"
print("5. str5.encode():", str5.encode())
# Roman: String ko bytes me convert karta hai
# Output: b'Siddiqui'

# 6. endswith(suffix)
str6 = "hello world"
print("6. str6.endswith('world'):", str6.endswith("world"))
# Roman: Check karta hai string suffix ke sath end hoti hai ya nahi
# Output: True

# 7. expandtabs(tabsize)
str7 = "Hello\tWorld"
print("7. str7.expandtabs(4):", str7.expandtabs(4))
# Roman: Tabs ko spaces me convert karta hai
# Output: "Hello   World"

# 8. find(substring)
str8 = "hello world"
print("8. str8.find('world'):", str8.find("world"))
# Roman: Substring ka first index return karta hai, nahi mile to -1
# Output: 6

# 9. format()
str9 = "My name is {}"
print("9. str9.format('Siddiqui'):", str9.format("Siddiqui"))
# Roman: Placeholder ko replace karta hai
# Output: "My name is Siddiqui"

# 10. format_map()
str10 = "My name is {name}"
print("10. str10.format_map({'name':'Siddiqui'}):", str10.format_map({"name":"Siddiqui"}))
# Roman: Dictionary se placeholders replace karta hai
# Output: "My name is Siddiqui"

# 11. index(substring)
str11 = "hello world"
print("11. str11.index('world'):", str11.index("world"))
# Roman: Substring ka first index return karta hai, nahi mile to error
# Output: 6

# 12. isalnum()
str12 = "Hello123"
print("12. str12.isalnum():", str12.isalnum())
# Roman: Check karta hai string sirf letters aur numbers se bani hai
# Output: True

# 13. isalpha()
str13 = "Hello"
print("13. str13.isalpha():", str13.isalpha())
# Roman: Check karta hai string sirf letters se bani hai
# Output: True

# 14. isascii()
str14 = "Hello"
print("14. str14.isascii():", str14.isascii())
# Roman: Check karta hai string ASCII characters se bani hai
# Output: True

# 15. isdecimal()
str15 = "123"
print("15. str15.isdecimal():", str15.isdecimal())
# Roman: Sirf decimal numbers check karta hai
# Output: True

# 16. isdigit()
str16 = "123"
print("16. str16.isdigit():", str16.isdigit())
# Roman: Sirf digits check karta hai
# Output: True

# 17. isidentifier()
str17 = "my_var"
print("17. str17.isidentifier():", str17.isidentifier())
# Roman: Valid Python identifier check karta hai
# Output: True

# 18. islower()
str18 = "hello"
print("18. str18.islower():", str18.islower())
# Roman: Sab letters lowercase hai ya nahi
# Output: True

# 19. isnumeric()
str19 = "123"
print("19. str19.isnumeric():", str19.isnumeric())
# Roman: Numeric characters check karta hai
# Output: True

# 20. isprintable()
str20 = "Hello\n"
print("20. str20.isprintable():", str20.isprintable())
# Roman: String print ke layak hai ya nahi
# Output: False

# 21. isspace()
str21 = "   "
print("21. str21.isspace():", str21.isspace())
# Roman: Sirf spaces check karta hai
# Output: True

# 22. istitle()
str22 = "Hello World"
print("22. str22.istitle():", str22.istitle())
# Roman: Har word ka first letter capital hai ya nahi
# Output: True

# 23. isupper()
str23 = "HELLO"
print("23. str23.isupper():", str23.isupper())
# Roman: Sab letters uppercase hai ya nahi
# Output: True

# 24. join(iterable)
str24 = "-"
print("24. str24.join(['S','i','d','d','i','q','u','i']):", str24.join(['S','i','d','d','i','q','u','i']))
# Roman: Iterable ko string ke sath join karta hai
# Output: "S-i-d-d-i-q-u-i"

# 25. ljust(width, fillchar)
str25 = "Hello"
print("25. str25.ljust(10,'*'):", str25.ljust(10,'*'))
# Roman: String left justify karta hai aur extra space fillchar se fill
# Output: "Hello*****"

# 26. lower()
str26 = "HELLO"
print("26. str26.lower():", str26.lower())
# Roman: String ko lowercase me convert karta hai
# Output: "hello"

# 27. lstrip()
str27 = "   Hello"
print("27. str27.lstrip():", str27.lstrip())
# Roman: Left side ke whitespaces remove karta hai
# Output: "Hello"

# 28. partition(sep)
str28 = "Siddiqui is great"
print("28. str28.partition('is'):", str28.partition("is"))
# Roman: Separator ke basis pe 3-tuple return karta hai (before, sep, after)
# Output: ('Siddiqui ', 'is', ' great')

# 29. replace(old,new)
str29 = "Hello Siddiqui"
print("29. str29.replace('Siddiqui','Friend'):", str29.replace("Siddiqui","Friend"))
# Roman: Old substring ko new substring se replace karta hai
# Output: "Hello Friend"

# 30. rfind(substring)
str30 = "Hello Siddiqui"
print("30. str30.rfind('i'):", str30.rfind("i"))
# Roman: Last occurrence ka index return karta hai
# Output: 12


# 31. rindex(substring)
str31 = "Hello Siddiqui"
print("31. str31.rindex('i'):", str31.rindex("i"))
# Roman: Last occurrence ka index return karta hai, nahi mile to error
# Output: 12

# 32. rjust(width, fillchar)
str32 = "Hello"
print("32. str32.rjust(10,'*'):", str32.rjust(10,'*'))
# Roman: String right justify karta hai aur extra space fillchar se fill
# Output: "*****Hello"

# 33. rpartition(sep)
str33 = "Siddiqui is great"
print("33. str33.rpartition('is'):", str33.rpartition("is"))
# Roman: Separator ke basis pe last occurrence ka 3-tuple return karta hai
# Output: ('Siddiqui ', 'is', ' great')

# 34. rsplit(sep)
str34 = "a,b,c,d"
print("34. str34.rsplit(',',2):", str34.rsplit(",",2))
# Roman: Right side se split karta hai aur list return karta hai
# Output: ['a','b','c','d']

# 35. rstrip(chars)
str35 = "Hello***"
print("35. str35.rstrip('*'):", str35.rstrip('*'))
# Roman: Right side ke specified characters remove karta hai
# Output: "Hello"

# 36. split(sep)
str36 = "a,b,c,d"
print("36. str36.split(','):", str36.split(','))
# Roman: Separator ke basis pe split karke list return karta hai
# Output: ['a','b','c','d']

# 37. splitlines(keepends)
str37 = "Hello\nWorld"
print("37. str37.splitlines():", str37.splitlines())
# Roman: Newline pe split karke list return karta hai
# Output: ['Hello','World']

# 38. startswith(prefix)
str38 = "Hello World"
print("38. str38.startswith('Hello'):", str38.startswith("Hello"))
# Roman: Check karta hai string prefix se start hoti hai ya nahi
# Output: True

# 39. strip(chars)
str39 = "***Hello***"
print("39. str39.strip('*'):", str39.strip('*'))
# Roman: Left aur right dono side ke specified characters remove
# Output: "Hello"

# 40. swapcase()
str40 = "Hello World"
print("40. str40.swapcase():", str40.swapcase())
# Roman: Uppercase to lowercase aur lowercase to uppercase karta hai
# Output: "hELLO wORLD"

# 41. title()
str41 = "hello world"
print("41. str41.title():", str41.title())
# Roman: Har word ka first letter uppercase karta hai
# Output: "Hello World"

# 42. translate(table)
import string
str42 = "Hello World"
table = str42.maketrans("HW","hw")
print("42. str42.translate():", str42.translate(table))
# Roman: Characters ko translate karta hai mapping table ke according
# Output: "hello world"

# 43. upper()
str43 = "hello"
print("43. str43.upper():", str43.upper())
# Roman: String ko uppercase me convert karta hai
# Output: "HELLO"

# 44. zfill(width)
str44 = "42"
print("44. str44.zfill(5):", str44.zfill(5))
# Roman: String ko zero se left pad karta hai
# Output: "00042"

# 45. isdecimal()
str45 = "123"
print("45. str45.isdecimal():", str45.isdecimal())
# Roman: Check karta hai ki string decimal characters se bani hai
# Output: True

# 46. isdigit()
str46 = "123"
print("46. str46.isdigit():", str46.isdigit())
# Roman: Check karta hai ki string digits se bani hai
# Output: True

# 47. isnumeric()
str47 = "123"
print("47. str47.isnumeric():", str47.isnumeric())
# Roman: Numeric characters check karta hai
# Output: True

# 48. isidentifier()
str48 = "my_var"
print("48. str48.isidentifier():", str48.isidentifier())
# Roman: Valid Python identifier check karta hai
# Output: True

# 49. islower()
str49 = "hello"
print("49. str49.islower():", str49.islower())
# Roman: Sab letters lowercase hai ya nahi
# Output: True

# 50. isupper()
str50 = "HELLO"
print("50. str50.isupper():", str50.isupper())
# Roman: Sab letters uppercase hai ya nahi
# Output: True

# 51. isspace()
str51 = "   "
print("51. str51.isspace():", str51.isspace())
# Roman: Sirf whitespaces check karta hai
# Output: True

# 52. istitle()
str52 = "Hello World"
print("52. str52.istitle():", str52.istitle())
# Roman: Har word ka first letter capital hai ya nahi
# Output: True

# 53. isprintable()
str53 = "Hello"
print("53. str53.isprintable():", str53.isprintable())
# Roman: String print ke layak hai ya nahi
# Output: True
