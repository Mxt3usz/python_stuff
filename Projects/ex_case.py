
def to_screaming_snake(s:str):
    string = ""
    for chars in s:
        if chars.islower():
            string += chars
        if chars.isupper():
            string += "_"
            string += chars
    return string.upper()



print(to_screaming_snake("mySuperCoolFunction"))

def to_camel(s:str):
    lower =  s.lower()
    string = []
    for chars in lower:
        string.append(chars)
    count = 0
    for c in string:
        count += 1
        if c == "_":
            string.pop(count - 1)
            string[count - 1] = c.upper()
    return "".join(string)



print(to_camel("MY_SUPER_COOL_FUNCTION"))
