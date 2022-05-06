import array

# array module!
arr = array.array('i', [1,2,3])
print(arr[0])

# we can always just do this anyway!
arr1 = [1,2,3]
print(arr1)

# append works in both
arr.append(4)
arr1.append(4)

print(arr[3])
print(arr1)

# so does insert!
arr.insert(3, 60)
arr1.insert(3, 60)

print(arr[3])
print(arr1)

# to print the contents of array created using array module:
for i in range(len(arr)):
    print(arr[i], end='\t')

print('\n')
