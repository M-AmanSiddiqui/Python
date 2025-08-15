# Python Numbers Method

# 📌 Integer (int) Methods
# Integers ke liye Python me mostly conversion methods hote hain:

# 1. bit_length()
# Integer ko binary me represent karne ke liye minimum bits kitne chahiye, ye return karta hai.


# x = 10
# print(x.bit_length())  # Output: 4  (binary = 1010)
# 2. to_bytes(length, byteorder, signed=False)
# Integer ko bytes me convert karta hai.


# x = 10
# print(x.to_bytes(2, 'big'))  # Output: b'\x00\n'
# 3. from_bytes(bytes, byteorder, signed=False) (class method)
# Bytes ko wapas integer me convert karta hai.


# print(int.from_bytes(b'\x00\n', 'big'))  # Output: 10
# 4. conjugate() (int me always self return hota hai)
# Complex number ka conjugate deta hai, int me same number deta hai.


# x = 5
# print(x.conjugate())  # Output: 5
# 5. real
# Real part return karta hai (int me khud number hota hai).


# x = 5
# print(x.real)  # Output: 5
# 6. imag
# Imaginary part return karta hai (int me 0 hota hai).


# x = 5
# print(x.imag)  # Output: 0
# 📌 Float Methods
# Floats me mostly math se related methods hote hain:

# 1. as_integer_ratio()
# Float ko fraction ke numerator/denominator me deta hai.


# x = 2.5
# print(x.as_integer_ratio())  # Output: (5, 2)
# 2. is_integer()
# Check karta hai float ka value integer hai ya nahi.


# x = 3.0
# print(x.is_integer())  # Output: True
# 3. hex()
# Float ko hexadecimal representation me deta hai.


# x = 3.5
# print(x.hex())  # Output: '0x1.cp+1'
# 4. fromhex(string) (class method)
# Hex string ko float me convert karta hai.


# print(float.fromhex('0x1.cp+1'))  # Output: 3.5
# 5. conjugate()
# Complex conjugate deta hai (float me same number return hota hai).


# x = 3.5
# print(x.conjugate())  # Output: 3.5
# 6. real
# Float ka real part return karta hai.


# x = 3.5
# print(x.real)  # Output: 3.5
# 7. imag
# Float ka imaginary part return karta hai (0 hota hai).


# x = 3.5
# print(x.imag)  # Output: 0
# 📌 Complex Number Methods
# 1. conjugate()
# Complex number ka conjugate return karta hai.


# z = 2 + 3j
# print(z.conjugate())  # Output: (2-3j)
# 2. real
# Real part return karta hai.


# z = 2 + 3j
# print(z.real)  # Output: 2.0
# 3. imag
# Imaginary part return karta hai.


# z = 2 + 3j
# print(z.imag)  # Output: 3.0