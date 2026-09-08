#programatically add odd nubers in between 20 and 40 into a list and display the numbers divisible ny 3
...
#make sure you can print numers 20 to 40
#from step1 print only odd numbers
#create a list and add all odd numbers on it
...

odd = []
for i in range(20, 41):
    if (i % 2 != 0):
        print(i)
        odd.append(i)
        
        if (i % 3 == 0):
          print(i)

#list comprehension

newlist2=[i for i in range(1,101) if (i%9 == 0)]
print(newlist2)

list1 = [num for num in range(1, 21)]
print(list1)