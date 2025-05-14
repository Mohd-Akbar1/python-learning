# python Data structure and boolean
print("python Data structure and boolean")

# print(type(True))
# print(type(False))

# print(True and False)
# print(True or False)
# print(not True)
# print(not False)

my_name='Mohd Akbar234'
print(my_name == 'Mohd Akbar')
print(my_name.capitalize())
print(my_name.upper())
print(my_name.lower())
print(my_name.title())
print(my_name.strip())
print(my_name.endswith('bar'))
print(my_name.startswith('m'))
print(my_name.isalnum())


#Boolean and logical operations
print("Boolean and logical operations")
#AND logics
print(True and False)
print(True and True)
print(False and False)

#or logics
print(True or False)
print(True or True)
print(False or False)

#list a collection of different items and it is mutablle
print("list a collection of different items and it is mutablle")
list=['one',3,True]
print(list)
print(list[0])
print(list[-1])
list[0]='two'
print(list)
print(len(list))


print('append and pop and insert')
print(list.append('four'))
print(list)
print(list.pop())
print(list)
print(list.pop(0))
print(list)
print(list.insert(0,'zero'))
print(list)


print("indexing and slicing")
print(list)
print(list[1:])
print(list[:2])
print(list[1:3])