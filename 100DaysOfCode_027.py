def roman_num_to_int(data):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    roman_special = {
        'IV': -2,
        'IX': -2,
        'XL': -20,
        'XC': -20,
        'CD': -200,
        'CM': -200,
    }
    normal_value = sum([roman[c] for c in data if c in roman])
    special_value = sum([value for key, value in roman_special.items() if key in data])
    return normal_value + special_value


print(roman_num_to_int('MMXXIV'))
