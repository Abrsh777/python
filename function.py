# function is basically a code,which performs a specific task. we type def to call a function.
def say_hi():
    print("Hello Users")
print("top")
say_hi()
print("bottom")
def say_hi(name,age):
    print("hello" + name + "you are " + str (age ))
say_hi("Mike", "12",)
say_hi("Abrsh", "32")



picture= [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
]
def show_tree():
 for row in picture:
   for pixel in row:
      if (pixel == 1):
         print("*", end="")
      else:
         print(" ", end="")
   print("")

show_tree()
show_tree()
show_tree()

     


