def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syms = [
        'M', 'CM', 'D', 'CD',
        'C', 'XC', 'L', 'XL',
        'X', 'IX', 'V', 'IV',
        'I'
        ]
    roman_numeral = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_numeral += syms[i]
            num -= val[i]
        i += 1
    return roman_numeral
num = int(input("Enter an integer: "))

# Convert the integer to a Roman numeral
roman_numeral = int_to_roman(num)

# Display the Roman numeral
print("Roman numeral:", roman_numeral)
