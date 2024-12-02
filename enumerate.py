for i,char in enumerate("Helloooo"): #numerate is useful we we want sth iterate from zero
 print(i,char)  


 for i,char in enumerate((1,2,3,4,5,6)): #numerate is useful we we want sth iterate from zero
  print(i,char)


for i,char in enumerate(list(range(100))): #numerate is useful we we want sth iterate from zero
    if char==50: 
     print(f"index of 50 is: {i}")