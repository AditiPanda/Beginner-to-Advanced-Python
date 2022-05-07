# Rotate an array of n elements by d positions to the left

arr1 = [1,2,3,4,5,6,7]
print(arr1)

d = 1
n = 7

temp = arr1[:d]
print(temp)

arr1_new = arr1[d:n] + temp
print(arr1_new)
