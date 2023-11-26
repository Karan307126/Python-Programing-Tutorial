# from array import *
from numpy import *
# from functools import reduce
# import project_02_the_perfect_guess     # i have import this python file as a module and use in this file.

# val = array('i', [5, 7, 8, 9, 10])

# print(val)  # for print simpaly array.

# for i in range(len(val)):   # this is one way to print array with help of for loop.
#     print(val[i])

# for i in val:   # this is another way to print to array with help of for loop.
#     print(i)

# i = 0
# while i < len(val):   # print array using while loop.
#     print(val[i])
#     i+=1

# val.reverse()
# for i in val:
#     print(i)

# print(val.buffer_info())  # printing the adrees and number of items in array.

# newArray = array(val.typecode, (a for a in val))  # copy array in another array.
# print(newArray)

# Taking value for array by user.
# arr = array('i', [])
# n = int(input("Enter the length of array : "))

# for i in range(n):
#     x = int (input("Enter the array values : "))
#     arr.append(x)

# print(arr)

# value = int (input("Enter the value serching : "))
# k = 0
# for e in arr:   # this is manual way to serching an element in array.
#     if e == value:
#         print(k)
#         break
#     k+=1
# else:
#   print("NOT FOUND!!")

# print(arr.index(value)) # this is built in function for sercching in array.

# arr1 = array([(1,2,3,4,5),(6,7,8,9,10)], int) # creating 2D array by numpy.
# print(arr1)

# arr3 = array([(1,2,3),(4,5,6),(7,8,9),(10,11,12)])
# print(arr3)
# print(arr3.ndim)

# arr12 = arr3.flatten()  # multi dimensnal array to single dimensnal array.
# print(arr12)

# arr13 = arr12.reshape(3, 2, 2)  # single dimensnal to multi dimensnal array.
# print(arr13)

# Other ways to decler array using numpy.
# arr4 = linspace(0, 10, 5)
# print(arr4)

# arr5 = logspace(1, 10, 2)
# print(arr5)

# arr6 = arange(0, 15, 2)
# print(arr6)

# arr7 = zeros(5, int)
# print(arr7)

# arr8 = ones(7, int)
# print(arr8)

# copy the array in another array.
# arr9 = array([1,2,3,4,5,6])
# print(arr9)

# arr10 = arr9.view() # sellow copy.
# print(arr10)

# arr11 = arr9.copy() # deep copy.
# print(arr11)

# matrix in array.
m1 = matrix('2 4 6 ; 7 9 3 ; 8 5 0')
m2 = matrix('4 5 1 ; 8 2 0 ; 3 7 9')
m3 = m1 + m2
m4 = m1 * m2
print(m3)
print(m4)

# function with variable length arguments.
# def person(name, **data):
#     print(name)
#     print(data)
#     for i, j in data.items():
#         print(i, j)

# person('Karan', age = 19, city = 'Ahmedabad', mob = 7435002910)

# print fibonachi series in python.
# def recFib(n):
#     if(n == 0 or n == 1):
#         return n
#     elif(n < 0):
#         print("INVALID INPUT!!")
#         return -1
#     else:
#         c = recFib(n - 1) + recFib(n - 2)
#         return c

# def itrFib(n):
#     a = 0
#     b = 1
#     if(n == 0):
#         print(a, end = " ")
#     elif(n == 1):
#         print(b, end = " ")
#     elif(n < 0):
#         print("INVALID INPUT!!")
#     else:
#         print(a, end = " ")
#         print(b, end = " ")
#         for i in range(2, n + 1):
#             c = a + b
#             print(c, end = " ")
#             a = b
#             b = c



# n = int(input("Enter the number : "))
# f1 = recFib(n)
# print(f1)
# f2 = itrFib(n)
# print(f2)

# factorial of given number.

# def itrFact(x):
#     f = 1
#     for i in range(1, n + 1):
#         f  *= i
#     return f

# def recFact(x):
#     if(x == 1 or x == 0):
#         return 1
#     return x * recFact(x - 1)

# n = int(input("Enter a number : "))
# result = itrFact(n)
# print(result)
# result2 = recFact(n)
# print(result2)

# lambda function or anonymous function.

# f = lambda a : a * a

# print(f(10))

# lambda(uses) with filter(), map() and reduce().

# nums = [3,6,2,8,0,1,7]

# even = list(filter(lambda a : a % 2 == 0, nums))
# print(even)

# double = list(map(lambda a : a * 2, even))
# print(double)

# sum = reduce(lambda a, b : a + b, double)
# print(sum)

# decoretor in python.
# decoretor use is change in inbuilt functions also.

# def div(a, b):
#     print(a / b)

# def smart_div(func):
#     def inner(a, b):
#         if a < b:
#             a, b = b, a
#         return func(a, b)
#     return inner

# div = smart_div(div)

# div(2, 4)