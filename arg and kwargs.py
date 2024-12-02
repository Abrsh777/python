def super_func(name,*args,i="hi", **kwargs):
    total= 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
    return sum(args) + sum(items in kwargs.values())
print (super_func("Abrsh",1,2,3,4,5, num1=5,num2=10))  


def highest_even(li):
    evens= []
    for item in li:
     if item % 2 ==0:
      evens.append(item)
    return max(evens)

print(highest_even([10,2,3,4,8,11]))



total=0
def count ():
   global total # global is used to access outside of our fun
   total += 1
   return total

count()
count()
print(count())





def multiply_by2(li):
   new_list=[]
   for item in li:
      new_list.append(item*2)
   return new_list
print(multiply_by2([1,2,3]))