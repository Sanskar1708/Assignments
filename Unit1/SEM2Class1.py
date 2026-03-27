list1 = ['a', 'b', 'c', 'd', 'z', 'k' ]
print(list1[1:3])
list1.append('e')
print(list1)
list1.remove('a')
print(list1)
list1.pop(-1)
print(list1)

list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1)
print(set2)

set3 = set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)


tup1 = ('a', 'b', 'c', 'd', 'e', 'f')
print(tup1[1:3])

tup2 = (tup1, 'g', 'h', 'i')
print(tup2)

print(tup1*3)

print(tup1 + tup2)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'e': 5, 'f': 6, 'g': 7, 'h': 8}

print(dict1['b'])

dict1.pop('d')
print(dict1)

dict3 = dict1 | dict2
print(dict3)

dict1.update(dict2)
print(dict1)