#1 Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element)
# Example: countdown(5) should return [5,4,3,2,1,0]

# def countdown(num):
#     arr = []
#     for x in range(num,-1,-1):
#         arr.append(x)
#     print(arr)
# countdown(5)

#2 Print and Return - create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def print_and_return(arr):
#     print(arr[0])
#     return arr[1]
# print_and_return([1,2])

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the lists length
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value + length: 5)
    
def first_plus_length(arr):
    return len(arr) + arr[0]
first_plus_length([1,2,3,4,5])

#4 Values greater than Second - write a function that accepts a list and creates a new list 
# containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list.
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def values_greater_than_second(thislist):
    newlist = []
    for i in range(len(thislist)):
     if  thislist[i] > thislist[1]:
         newlist.append(thislist[i])
    print(len(newlist))
    return thislist[i]

#5 This length, That Value - write a function that accepts two integers as parameters: sizze and value. The function should
# create and return a list whose length is equal to the given size, and whose values are the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(size,value):
    newList = []
    for i of range(0, size):
        newlist.append(value)
    return newList[i]


(4,7)


