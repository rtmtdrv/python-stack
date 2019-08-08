# #1 Basic - print all integers from 0 to 150
for x in range(150):
    print(x)

# #2 Multiples of Five - print all the multiples of 5 from 5 to 1,000
for x in range(5, 1000, 5):
    print(x)

# #3 Counting, the Dojo Way - print integers 1 to 100. 
# #  If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding "Dojo
for x in range(1,100):
    if x % 10 == 0:
        print("Coding") 
    elif x % 5 == 0:
        print("Dojo")
    else:
        print(x)

#4 Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum
# total = 0
for x in range(1,500000,2):
    total += x
    print(x, total)

#5 Countdown by Fours - print positive numbers starting at 2018, counting down by fours
x = 2018
while x > 0:
    print(y)
    x = x - 4

#6 Flexible Counter - set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only
#  the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should
#  print 3, 6, 9 (on successive lines) 

lowNum = x
highNum = y
mult = z
for i in range(x, y+1):
    if i % z == 0:
    print(i)


