a = 52  # decimal
b = 0x25  # hexadecimal
c = 0x45  # hexadecimal

# Print the values
print("a (decimal):", a)
print("b (hexadecimal):", hex(b))
print("c (hexadecimal):", hex(c))

# Perform bitwise AND between a and b
and_result = a & b
print("a & b (bitwise AND):", and_result)

# Perform bitwise OR between the result and c
or_result = and_result | c
print("(a & b) | c (bitwise OR with c):", or_result)

# Print the values in binary and hexadecimal
print("Binary values:")
print("a:", bin(a))
print("b:", bin(b))
print("c:", bin(c))
print("a & b:", bin(and_result))
print("(a & b) | c:", bin(or_result))
print("Hexadecimal values:")
print("a:", hex(a))
print("b:", hex(b))
print("c:", hex(c))
print("a & b:", hex(and_result))
print("(a & b) | c:", hex(or_result))