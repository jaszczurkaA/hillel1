
def roman_to_integer(s):

    roman_to_arabian = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900, 'M':1000}
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in roman_to_arabian:
            num += roman_to_arabian[s[i:i+2]]
            i+=2
        else:
            num += roman_to_arabian[s[i]]
            i+=1
    return num

print(roman_to_integer('DCIX'))
