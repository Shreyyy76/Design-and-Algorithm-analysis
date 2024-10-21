def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2 
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    P1 = karatsuba(high_x, high_y)
    P2 = karatsuba(low_x, low_y)
    P3 = karatsuba(high_x + low_x, high_y + low_y) - P1 - P2
    return P1 * 10**(2*m) + P3 * 10**m + P2
x = 1234
y = 5678
result = karatsuba(x, y)
print(f"The product of {x} and {y} is: {result}")
