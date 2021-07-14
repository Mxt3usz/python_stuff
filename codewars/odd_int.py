def find_it(seq):
    count_nums = - 1
    count_num = len(seq)
    lst = {}
    last_seen = None
    for nums in seq:
        invalid = False
        if last_seen == nums:
            invalid = True
        count_nums += 1
        for num in seq[::-1]:
            count_num += -1
            if count_num == count_nums and len(seq) > 1:
                count_num = len(seq)
                break
            if nums == num:
                if num not in lst:
                    lst.__setitem__(num,1)
                else:
                    if  invalid == False:
                        lst[num] +=1
                        last_seen = nums
    for keys in seq:
        if keys not in lst:
            return keys
    for key,value in lst.items():
        if len(lst) == 1:
            return key
        for k,v in lst.items():
            if k != key and v != value:
                return k

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))
print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))
print(find_it([10]))
print(find_it([1,1,1,1,1,1,10,1,1,1,1]))
print(find_it([5,4,3,2,1,5,4,3,2,10,10]))
print(find_it([4,3,2,4,3,1,132,5,132,2,5,10,8,10,1]))

