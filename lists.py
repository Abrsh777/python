friends= ["abrsh","haileye","jackson","mesafint", "NF"] # abrsh index of 0, haileye 1, jackson 2 or wecan use negetives -1 is jackson, index -2 is haileye
print(friends)
print(friends [2])
print(friends [0])
print(friends [-1])
print(friends [1:3])
print(friends [0:5])
print ("abrsh" in friends)
print ("elias " in friends)

print (friends[1])


# list function


luckey_numbers= [4,8,14,17,21,43] 
friends= ["abrsh","haileye","jackson","mesafint", "NF"] 
friends.extend(luckey_numbers)
print(friends)
friends.append("elias")
print(friends)
friends.insert(1,"mj")
print(friends)
friends.remove("jackson")
print(friends)

friends.pop()

print(friends)
friends.clear()
print(friends)
friends= ["abrsh","haileye","jackson","mesafint", "NF"] 
print(friends.index("abrsh"))
friends= ["abrsh","haileye","jackson","abrsh","abrsh", "mesafint", "NF"] 
print(friends.count("abrsh"))
friends.sort()
print(friends)
luckey_numbers.reverse()
print(luckey_numbers)
friends2= friends.copy()
print(friends2)


print(list(range(1,100)))


#list unpacking
a,b,c, *other,d=[1,2,3,4,7,8,9]
print(a)
print(b)

print(c)
print(other)

#print(d)
#print("ytiyvi")
#print(int(2*5))