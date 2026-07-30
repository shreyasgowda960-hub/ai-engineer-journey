nums = [1, 2, 3, 2, 4, 2, 5, 1]

unique_nums=[]

counts=[]

for x in nums:
    if x in unique_nums:
        y = unique_nums.index(x)
        counts[y] = counts[y] + 1
    else:
        unique_nums.append(x)
        counts.append(1)

print(unique_nums)
print(counts) 