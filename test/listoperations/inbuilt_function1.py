#sort -sorts the elements in the list
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
cities.sort()
print(cities)

numbers=[5, 3, 8, 1, 2,2]
numbers.sort()
print(numbers)

# count - provides the count of duplicate elements
numbers.count(3)
print(numbers.count(2))
print(numbers.count(5))

#list extend
cities=["Mysore","Hassan",45,100,True,10.75,False,"Sira"]
more_cities=["Bangalore","Mangalore"]
cities.extend(more_cities)
print(cities)

#Index - provides the index of the first occurrence of an element
print(cities.index("Hassan"))
print(cities.index("Sira"))

#copy list 
cities_copy = cities.copy()
print(cities_copy)  


#reverse - reverses the elements in the list
cities.reverse()
print(cities)   
