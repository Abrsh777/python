# return statement can allow us to do the return keyword can basically 
# allow python to return information from the function. 
# should do one thing reallywell,
#should return something

def cube(num):
    return  num*num*num

print(cube(3))   

def cube(num):
    return  num*num*num
result= cube(4)
print(result)   


def sum(num1,num2):
   return num2 + num1
print (sum(4,5))




def sum(num1,num2):
   def another_func(n1, n2):
    return n1 + n2
   return another_func(num1,num2)
total= sum (10,20)
print (total)

