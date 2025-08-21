# before
old_list = [1,2,3,4,5]
result = []
for i in old_list:
    if i % 2 == 0:
        result.append(i)

print(result)

# comprehension
result = [i for i in old_list if i % 2 == 0]
print(result)
