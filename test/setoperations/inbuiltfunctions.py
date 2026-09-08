#inbuilt functions

set1={"Apple","Mango", 100,300,"Lotus","Camel",True, False, 12.75}
print(set1)

#copy
elements = set1.copy()
print(elements)

#pop - removes from start
elements.pop()
print(elements)

print("--------------")

#remove -
print(set1)
set1.remove(300)
print(set1)

#clear
set1.clear()
print(set1)

