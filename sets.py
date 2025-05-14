# set , a set is a collection of unordered data type that is iterable ,mutbale and has no duplicates base on hash table
# there is no indexing in set
print('set')
myset=set()

myset.add(1)
print(type(myset))
print(myset)

test={1,2,2,3}
test.add(4)
print(test)


# dictionaries
# dictionaries are collection of key value pair
# dictionaries are mutable
# dictionaries are unordered
# dictionaries are iterable
dict={}

my_dict={'key1':'value1','key2':'value2'}
print(type(dict))
print(my_dict.keys())

for x in my_dict:
    print(x)

for x in my_dict.values():
    print(x)

for x,y in my_dict.items():
    print(x,y)


print(my_dict.items())
my_dict['key3']='value3'
print(my_dict.items())

my_value={'key1':'value1','key2':'value2','key3':'value3'}
my_dict['key4']=my_value
print(my_dict)