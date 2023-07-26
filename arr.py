import array as ar

array_1 = ar.array ('i',[1, 2, 3])
print(array_1)
for i in array_1:
    print(i)



list_1 = [4, 5, 6]

for i in list_1:
    array_1.insert(3+1, i)

print(array_1)
array_1.append(8)
print(array_1)

print(array_1.index(8))

#when popping in an array you can insert an index.
array_1.pop()
print(array_1)
array_1.remove(5)
print(array_1)