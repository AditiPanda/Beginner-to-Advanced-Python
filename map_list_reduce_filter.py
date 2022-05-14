org_list = [1,2,3,4,5]

fin_list = []

for num in org_list:
    fin_list.append(num**3)

print(fin_list)


##################
print('Using Maps!!')

def cube(num):
    return num**3

fin_list_new = []

fin_list_new = list(map(cube, org_list))
print(fin_list_new)

######################
print('Using Maps and Lambda too!!')

fin_list_new_1 = []

fin_list_new_1 = list(map(lambda x:x**3, org_list))
print(fin_list_new_1)
####################

base = [1,2,3,4]
power = [1,2,3,4]

ans_list = []

ans_list = list(map(lambda x,a:x**a, base, power)) # can use pow function instead
print(ans_list)

org_list = ['lana', 'del', 'rey', 'random']
ans_list = list(map(len, org_list))
print(ans_list)

# map,filter,reduce - each expect a function object as the first argument.
# functions passed to map(), filter(), and reduce() are the ones you'd use only once,
# so there's often no point in defining a referenceable function.
# so lambdas are used to define short, disposable, anonymous functions.

fruits = ['Apple', 'Banana', 'Apricot', 'Pears','Orange']
truth_list = list(map(lambda s:s[0]=='A', fruits))
print(ans_list)

fruit_truth_list = list(filter(lambda s:s[0]=='A', fruits))
print(fruit_truth_list)

from functools import reduce
num_list = [2, 4, 6, 3]
sum_value = reduce(lambda x,y:x-y, num_list)
print(sum_value)

sum_with_init = reduce(lambda x,y:x-y, num_list, 100)
print(sum_with_init)
