"""             1
			1		1
		1		2		1
	1		3		3		1
1		4		6		4		1

Implementation of Pascal Triangle
"""

def pascal(n : int):
    pascal_form = []
    for number in range(1, n + 1):
        if number == 1 or number == 2:
            pascal_form += [1]
    return pascal_form






print(pascal(0))
print(pascal(1))
print(pascal(2))
print(pascal(3))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
