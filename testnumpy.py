# numpy 
# Numpy is a general purpose array-processingpacakge
# Numpy provides a high-performance multidimensional container of generic data

# pip install numpy
import numpy as np

my_list=[1,2,3]
my_array=np.array(my_list)
print(my_array)

print(type(my_array))


# helps to specify how many number of rows and columns
print(my_array.shape)




#multidimensional array
list1=[1,2,4,6]
list2=[4,2,46,7]
list3=[6,1,8,4]
arr=np.array([list1,list2,list3])
print(arr)

print(arr.shape)


# 2 brackets opening and closing defines 2d array same as 2d matrix
#print(arr.ndim)


# array can be reshaped based on total count of elements

print(arr.reshape(6,2))
print(arr.reshape(4,3))


# acessing indexs
list=np.array([1,2,3,4,5,6])
print(list[5])
print(arr[1][1])

print('----------------------------------------------------')

#slicing
print(arr[:,:])
print(arr[1:3,1:3])
print(arr[1:,2:])

print('------------------arrange----------------------------------')

#arrange
arr=np.arange(5,11,step=2)
print(arr)

print('------------------linspace----------------------------------')

#linspace
arr=np.linspace(1,10,50)
print(arr)


print('------------------copy----------------------------------')

#copy
arr=np.array([1,2,3,4])
print(arr)

arr1=arr.copy()
arr1[2:]=4
print(arr1)


# condtitions
print('------------------conditions----------------------------------')

arr=np.array([1,2,3,4])
print(arr>2)
print(arr[arr>2])

#ones
print('------------------ones----------------------------------')

arr=np.ones((2,3))
print(arr)

arr=np.zeros((4,4),dtype=float)
print(arr)


#empty
print('------------------empty----------------------------------')

arr=np.empty((4,4))
print(arr)


# random distribution
print('------------------random distribution----------------------------------')

arr=np.random.random((2,4))
print(arr)


# random integers
print('------------------random integers----------------------------------')

arr=np.random.randint(5,10,9).reshape(3,3)
print(arr)

#randn
print('------------------randn----------------------------------')

arr=np.random.randn(3,4)
print(arr)