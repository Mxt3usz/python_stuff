"""
Normal Way
"""
def ctof(temp:float) -> float:
    return  (9/5) * temp + 32

def list_ctof(cl:list[float])->list[float]:
    result = []
    for celsius in cl:
        result += [ctof(celsius)]
    return result

c_lst = [20,30,10,-1,-20]
f_lst =  list_ctof(c_lst)
print(f_lst)

maped = list(map(ctof,c_lst))
print(maped)
maped_1 = list(map(lambda c : 1.8 * c + 32,c_lst))
print(maped_1)
def gen(cl):
    for x in cl:
        yield ctof(x)

genrator = list(gen(c_lst))
print(genrator)
