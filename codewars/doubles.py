def duplicate_count(text):
    doubles = []
    cc = -1
    c = len(text)
    for chars in text:
        cc += 1
        for char in text[::-1]:
            c -= 1
            if cc == c:
                c = len(text)
                break
            if chars.lower() == char.lower():
                if chars.lower() in doubles:
                    continue
                else:
                    doubles += [chars.lower()]
    print(doubles)
    return len(doubles)

print(duplicate_count("Ws8IvclCnEmNTVnkSQABt8cw6Olv3g4"))
