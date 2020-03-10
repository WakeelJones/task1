numbers = [56,78,34,21,56,34,125,45,89,75,12,56]
print(type(numbers))
len_list = len(numbers)
sum1 = 0
while len_list != 0:
    sum1 += numbers [0]
    len_list -= 1

print(sum1)
print(numbers)
numbers.sort()
print(numbers)
print("smallest element is:", min(numbers))
print("largest element is:", max(numbers))

dup_items = set()
uniq_items = []
for x in numbers:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)