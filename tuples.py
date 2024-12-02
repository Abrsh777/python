# tuples is a type of data stracture, which basically means it is a container where we can store different values.
#  it is basically store multiple information. tuple is different from lists. examples of tubles xy coordinates. 
# turples are immutable. which means we can not change or modifieed it.


coordinates= (4,5)
print (coordinates)
print (coordinates [0])
coordinates=[(4,5),(6,7),(12,10)]
print (coordinates)


my_turple= (1,2,3,4,5)
new_tuple= my_turple[1:4]
print(new_tuple)


x,y,z, *other= (1,2,3,4,5,5)
print(y)  
print(other)
print(x,y,z, *other.count(5))

