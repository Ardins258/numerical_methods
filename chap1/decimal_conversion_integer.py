# This code provides a way of converting from base10(Decimal) 
# and is only valid for numbers [1, oo)
# Base 2 ( Binary )
# Base 8 ( Octal )
# Base 16 ( HexaDecimal )
# and etc.
# Import lib
from math import log

def cfb10(num, base): # cfb10 = convert from base 10
    # Create conversion dic
    numtochar = {i:"0123456789ABCDEF"[i] for i in range(16)}
    # Set power to largest
    power = int(log(num,base))
    # Convert number
    converted = ""
    for pow in range(power, -1, -1):
        # Divide
        converted += numtochar[num // (base**pow)]
        # Remainder
        num %= base**pow
    return converted
print(cfb10(429, 7)) # ( number in base 10 first, to base =" )
print(cfb10(18238, 16))
print(cfb10(25, 2))

