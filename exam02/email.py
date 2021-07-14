def is_mail_adress(mail:str):
    email = True
    a = []
    for c in mail:
        a += [c]
    c_a = 0
    index = -1
    index_a = 0
    for x in a:
        index += 1
        if x == "@":
            c_a += 1
            index_a = index + 1
            if a[index - 1] == ".":
                print("fehler")
                email = False
    if c_a > 1 or c_a == 0:
            print("Fehler")
            email = False
    index_x = -1
    count_p = 0
    index_p  = 0
    lst = []
    for x in a[index_a:]:
        lst += [x]
        index_x += 1
        if index_x == 0 and x == ".":
            print("Fehler")
            email = False
        if x == ".":
            count_p += 1
            index_p = index_x + 1

    if len(lst[index_p:]) < 2:
        email = False

    return email


print(is_mail_adress("mateuszgawior@yahoo.de"))
