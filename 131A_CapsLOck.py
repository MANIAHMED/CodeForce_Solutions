str = input()

if str.isupper():
    str=str.lower()
    print(str)
elif str[1:].isupper():
    str=str.swapcase();
    print(str)
elif len(str)==1 and str.islower():
    str=str.swapcase()
    print(str)
else:
    print(str)
