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
print('Appending..')
print(arr[3])
print(arr1)

# so does insert!
arr.insert(3, 60)
arr1.insert(3, 60)
print('Inserts!')
print(arr[3])
print(arr1)

# to print the contents of array created using array module:
for i in range(len(arr)):
    print(arr[i], end='\t')
print('\n')

# pop(pos) - to remove elt at pos
print('Waz popping?')
arr.pop(3)
for i in range(len(arr)):
    print(arr[i], end='\t')
print('\n')

arr1.pop(3)
print(arr1)

# remove(elt) removes 1st occurence of elt
arr.append(1)
arr1.append(1)
print('Removals..!')
arr.remove(1)
for i in range(len(arr)):
    print(arr[i], end='\t')
print('\n')
arr1.remove(1)
print(arr1)


# index(elt) gives the index of 1st occurence of elt
print('Index!!!!')
print(arr.index(3))
print(arr1.index(3))

# reversing an array in python
print('Reversing!!')
arr.reverse()
for i in range(len(arr)):
    print(arr[i], end='\t')
print('\n')
arr1.reverse()
print(arr1)
