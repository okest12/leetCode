def find_addend(nums, target):
    c_index = {}
    for i, c in enumerate(nums):
        if target - c in c_index:
            return [c_index[target - c], i]
        c_index[c] = i


print(find_addend([1,3,5,7],10))