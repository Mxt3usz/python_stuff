def unique_in_order(iterable):
    lst =  []
    try:
        for i in range(0,len(iterable)):
            if iterable[i] != iterable[i+1]:
                lst += iterable[i]
    except Exception:
        lst += iterable[i]
    return lst
#def unique_in_order(iterable):
    #result = []
   # prev = None
  #  for char in iterable[0:]:
       # if char != prev:
      #      result.append(char)
     #       prev = char
    #return result


print(unique_in_order("AAAABBBCCDAABBB"))
print(unique_in_order("ABBCcAD"))
print(unique_in_order([1,2,2,3,3]))
