#set operations union,

set1 = {"Mango", "Apple", "Banana"}
set2 = {"Banana", "Grapes", "Orange"}

union_set = set1.union(set2)
print(union_set)

#another way to get union
union_set2 = set1 | set2
print(union_set2)

#intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)

#another way to get intersection
intersection_set2 = set1 & set2
print(intersection_set2)

#difference of sets
difference_set = set1.difference(set2)
print(difference_set)

#another way to get difference
difference_set2 = set1 - set2
print(difference_set2)

#symmetric difference of sets - inverse of intersect
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)

#another way to get symmetric difference
symmetric_difference_set2 = set1 ^ set2
print(symmetric_difference_set2)    

