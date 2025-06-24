# Let's study data structures like list, tuple and set today

# Lists : Ordered, Mutuable 

names=['avantika','sejal','saurabh','laksmikant']
ages=[22,21,34]
fav=[23.4,67.5,87.9,54.8]

print(names)

print(names[2])
# print(names[4])   index error
print(ages[-1])
print(fav[0])

names[2] = "arpan"

print(names[2])

print(names[0:2])
print(fav[::-1])
print(ages[:1])

# List methods
bts=['Dynamite', 'Butter','Boy with luv', 'Fake Love']
print("Original list:",bts)

bts.append('Mic Drop')
print("After appending new item:",bts)

bts.insert(1,'Fire')
print("After insert:", bts)

bts.remove('Butter')
print("After remove:", bts)

last_item=bts.pop()
print("Popped item", last_item)
print("After pop:", bts)

bts.sort()
print("Afetr sort:", bts)

bts.reverse()
print("After reverse:", bts)

#nested list

kpop=[['Dynamite','Butter','DNA'],['What is luv','The Feels','Fancy'],['Pretty u','super','Aju Nice']]
print(kpop[0][1])
print(kpop[2])

kpop[0][2]= 'Dimple'
kpop.append(['sugar rush hour','run away','magic'])
print(kpop)

#tuples: Ordered, Immutauable

numbers=(88, 76, 54, 99, 32)
colors=('red', 'green', 'blue')

print(numbers[0])
print(colors[2])

print(numbers[1:3])

#colors[1] = 'Black' # TpyeError

lists=[65, 78, 90, 34]
tuples=tuple(lists)
print(tuples)

#Sets: Unordered, No Duplicates, Mutuable

fruits={'apple', 'banana', 'cherry', 'apple', 'guava'}
print(fruits)

#print(fruits[0])    #TypeError

fruits.add("grapes")
print('After Adding:', fruits)

fruits.remove("apple")
print("After removing", fruits)

num1={1, 3, 5, 7}
num2={4, 5, 8, 1}

print(num1.union(num2))
print(num1.intersection(num2))


