#************************************Python Number Methods**************************************#

# 1. bit_length()
num1 = 10
num1_bit_length = num1.bit_length()
print("1. num1.bit_length():", num1_bit_length)
#  Number ko binary me represent karne ke liye required bits ka count return karta hai
# Output: 4 (10 ka binary: 1010 => 4 bits)

# 2. conjugate()
num2 = 3+4j
num2_conjugate = num2.conjugate()
print("2. num2.conjugate():", num2_conjugate)
#  Complex number ka conjugate return karta hai
# Output: (3-4j)

# 3. as_integer_ratio()
num3 = 2.5
num3_ratio = num3.as_integer_ratio()
print("3. num3.as_integer_ratio():", num3_ratio)
#  Float ko fraction me convert karta hai (numerator, denominator)
# Output: (5, 2)

# 4. is_integer()
num4 = 3.0
num4_is_integer = num4.is_integer()
print("4. num4.is_integer():", num4_is_integer)
#  Check karta hai number integer type ka hai ya nahi
# Output: True

# 5. real
num5 = 5+6j
num5_real = num5.real
print("5. num5.real:", num5_real)
#  Complex number ka real part return karta hai
# Output: 5.0

# 6. imag
num6 = 5+6j
num6_imag = num6.imag
print("6. num6.imag:", num6_imag)
#  Complex number ka imaginary part return karta hai
# Output: 6.0

# 7. __add__()
num7_a = 5
num7_b = 3
num7_add = num7_a.__add__(num7_b)
print("7. num7_a.__add__(num7_b):", num7_add)
#  Addition operation ka special method
# Output: 8

# 8. __sub__()
num8_a = 10
num8_b = 4
num8_sub = num8_a.__sub__(num8_b)
print("8. num8_a.__sub__(num8_b):", num8_sub)
#  Subtraction ka special method
# Output: 6

# 9. __mul__()
num9_a = 6
num9_b = 7
num9_mul = num9_a.__mul__(num9_b)
print("9. num9_a.__mul__(num9_b):", num9_mul)
#  Multiplication ka special method
# Output: 42

# 10. __truediv__()
num10_a = 15
num10_b = 4
num10_div = num10_a.__truediv__(num10_b)
print("10. num10_a.__truediv__(num10_b):", num10_div)
#  Division ka special method (float result)
# Output: 3.75

# 11. __floordiv__()
num11_a = 15
num11_b = 4
num11_fdiv = num11_a.__floordiv__(num11_b)
print("11. num11_a.__floordiv__(num11_b):", num11_fdiv)
#  Floor division (integer result) ka method
# Output: 3

# 12. __mod__()
num12_a = 17
num12_b = 5
num12_mod = num12_a.__mod__(num12_b)
print("12. num12_a.__mod__(num12_b):", num12_mod)
#  Modulus operation ka method
# Output: 2

# 13. __pow__()
num13_a = 2
num13_b = 5
num13_pow = num13_a.__pow__(num13_b)
print("13. num13_a.__pow__(num13_b):", num13_pow)
#  Power operation ka method
# Output: 32

# 14. to_bytes()
num14 = 255
num14_bytes = num14.to_bytes(2, byteorder='big')
print("14. num14.to_bytes(2,'big'):", num14_bytes)
#  Number ko bytes me convert karta hai
# Output: b'\x00\xff'

# 15. from_bytes()
num15_bytes = b'\x00\xff'
num15_from_bytes = int.from_bytes(num15_bytes, byteorder='big')
print("15. int.from_bytes(b'\\x00\\xff','big'):", num15_from_bytes)
#  Bytes ko integer me convert karta hai
# Output: 255
