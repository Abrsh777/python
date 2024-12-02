# for loop is aspecial type of loop in Python, which allows
#  us to loop over different collections of items. and we use 
# for loop through differnt arrays, or we can loop over like the
#  letters inside of the string, or we could just loop through like a series of numbers.
for letter in "Abrsh Academy":
    print (letter)
    print (letter)
    print (letter)


friends= ["Jim","Karen","Kevin"]
for friend in friends:
    print (friend)

    friends= ["Jim","Karen","Kevin"]
for name in friends:
    print (name)
for index in range (10):
    print(index)
for index in range (3,10):
    print(index)

friends= ["Jim","Karen","Kevin"]
len(friends)
for index in range (len(friends)):
    print(friends[index])
    friends[2]  


friends= ["Jim","Karen","Kevin"]
len(friends)
for index in range (5):
    if index == 0:
        print ("first iteration")
    else:
        print("not first")

    



for item in (1,2,3,4,5):
 for x in ["a","b","c"]:
    print(item, x)

user={"name":"Abrsh ",
      "age":23,
    "can_swim":False }
for item in user():
    print(item)
for item in user.items():
    print(item)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)