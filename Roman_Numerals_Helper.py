import re
class RomanNumerals:
    def __init__(self):
        self.dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def to_roman(self, num):
        result = ''
        for key, value in self.dict.items():
            result += (num // key) * value
            num = num % key
        return result

    
    def from_roman(self, str):
        result = 0
        i = 0
        while i < len(self.dict):
            reg = '^' + list(self.dict.values())[i]
            if re.search(reg, str) != None:
                result += list(self.dict.keys())[i]
                str = re.sub(reg,'',str) 
            else:
                i += 1
        return result

if __name__ == '__main__':
    RomanNumerals = RomanNumerals()
    print(RomanNumerals.to_roman(1666))
    print(RomanNumerals.from_roman('MDCLXVI'))
    print(RomanNumerals.from_roman('XXI'))
    print(RomanNumerals.from_roman('IV'))
