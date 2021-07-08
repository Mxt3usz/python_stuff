


matrix = []
for rows in range(3):
    row = []
    for i in range(rows *3,rows*3 + 3):
        row += [i+1]
    matrix += [row]

a = [list(range(y*3+1,y*3+4)) for y in range(3)]
print(a)
a2 = [[x + y for x in range(1,4)] for y in range(0,9,3)]
print(a2)
