my_set= {1,2,3,4,5,5} #when we print the variable, there is no repetation 
print(my_set)
my_set.add(100)
print(my_set)



my_list= [1,2,3,4,5,5] #when we print the variable, there is no repetation 
print(set(my_list))  


my_set1= {1,2,3,4,5}
your_set= {4,5,6,7,8,9,10}
print(my_set1.difference(your_set ))   
print(my_set1.discard(2 ) ) 
print(my_set1) 
 
print(my_set1.intersection(your_set ))   
print(my_set1.isdisjoint (your_set ))   
print(my_set1.union(your_set ))  #or
print(my_set1 | your_set) 
print(my_set1 & your_set )
print(my_set1.issubset(your_set ))   
print(your_set.issuperset(my_set1 )) 



