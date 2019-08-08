#1  #Biggie Size - Given a list, write a function that changes all 
# positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, 
# but whose values are now [-1, "big", "big", -5]

def biggie_size(thislist):
    for i in range(len(thislist)):
        if thislist[i] > 0:
            thislist[i] = "big"
    return thislist
print(biggie_size([-1, 3, 5, -5]))

#2 Count Positives - Given a list of numbers, create a function to 
# replace the last value with the number of positive values. 
# (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(p_list):
    count = 0
    for i in range (0, len(p_list)):
        if p_list[i] > 0:
            count += 1
    p_list[len(p_list)-1] = count
return p_list


#3 Sum Total - Create a function that takes a list and returns the sum of all the 
# values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(sum_list):
    sum = 0
    for i in range (0,len(sum_list)):
        sum+= sum_list[i]
    print(sum)

print(sum_total([1, 2, 3, 4]))

#4 Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5

def average(thislist):
    sum = 0
    for i in range(len(thislist)):
        sum += thislist[i]
    sum = sum/len(thislist)
    return sum

# print(average([1, 2, 3, 4]))

def average(thislist):
    sum = 0
    for i in range(len(thislist)):
        sum  += thislist[i]
    sum = sum / len(thislist)
    return sum

print(average([1,2,3,4]))

#5 Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def lengthofarray(newlist):
    if len(newlist) == 0:
        return false
        return len(newlist)
print(lengthofarray([]))

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def min(m_list):
    min = min_list[0]
    if len(m_list) == 0:
        return False
    else:
    for i in range (len(m_list)):
        if m_list[i] < min:
            min = min_list[i]
    return min

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

# def maximum(thislist):
#     max = 0
#     for i in range(len(thislist)):
#         if thislist[i] > max:
#             max = thislist[i]
#         else thislist[i] == []:
#             return False
#     return max

# print(maximum([]))

def max(m_list):
    if len(m_list) == 0:
        return False
    else: 
        max = m_list[0]
        for i in range(0, len(m_list)):
            if m_list[i] > max:
                max = m_list
        return max
print (max([]))
print(max([37,2,1,-9]))

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9])
# should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def analysis(p_list):
    max = p_list[0]
    min = p_list[0]
    sum = 0
    for i in range(0, len(p_list)):
        if p_list[i] > max:
            max = p_list[i]
        if p_list[i]< min:
            min = p_list[i]
        sum = sum + p_list[i]
        avg = sum / len(p_list)
        length = len(p_list)
        analysis = {
            'max': max,
            'min': min,
            'sum': sum,
            'avg': avg,
            'length': length
        }
    return analysis

print(analysis([37,2,1,-9]))

#9 Reverse List - Create a function that takes a list and return that list with 
#values reversed. Do this without creating a second list. (This challenge is known to appear 
# during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(a_list):
    for i in range(int(len(a_list)/2)):
        temp = a_list[i]
        a_list[i] = a_list[len(a_list)-1-i]
        a_list[len(a_list)-1-i] = temp
    return a_list

print(reverse_list([37,2,1,-9]))