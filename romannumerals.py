def romanToInt(s: str) -> int:
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0

    if 'IV' in s:
        total += 4
        s = s.replace('IV', ' ')
    if 'IX' in s:
        total += 9
        s = s.replace('IX', ' ')
    if 'XL' in s:
        total += 40
        s = s.replace('XL', ' ')
    if 'XC' in s:
        total += 90
        s = s.replace('XC', ' ')
    if 'CD' in s:
        total += 400
        s = s.replace('CD', ' ')
    if 'CM' in s:
        total += 900
        s = s.replace('CM', ' ')

    for char in s:
        if char == " ":
            continue
        else:
            total += roman_numerals[char]

    return total


print(romanToInt("MCMXCIV"))
