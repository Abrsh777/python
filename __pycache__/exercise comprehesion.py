some_list= ["a","b","c","b","d","m","n","n"]
duplicates= []
for value in some_list:
    if some_list.count(value)>1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)





some_list=list(set (["a","b","c","b","d","m","n","n"]))
duplicates= [x for x in some_list if some_list.count(x)>1  ] 
print(duplicates)
