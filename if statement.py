is_male = False
is_tall= False
if is_male or is_tall:
   
    print (" you are a male or tall or both") 

else:
     print ("you are neither male nor tall") 



is_male =False
is_tall= True
if is_male and is_tall:
   
    print ("you are a tall male") 
elif is_male and not(is_tall):
    
    print("you are a short male")
elif not(is_male )and is_tall:
    print("you are not a male but you are tall")
else:
     print ("you are neither male nor tall") 



     # if statement and comparision

def max_num(num1, num2, num3):
 if num1 >= num2 and num1 >= num3:
        return num1 
 elif num2 >= num1 and num2 >= num3:
     return num2
 else:
     return num3
 
print (max_num(3,4,5))
print (max_num(3,43,25))


 
     
 
 