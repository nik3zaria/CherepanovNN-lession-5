src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = []
for nums in src:
    if (nums in result) and (nums in src):
        result.remove(nums)
    else:
        result.append(nums)

print(result)
