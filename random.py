# dict ={
#     frozenset({1,2}): 3,
#     frozenset({4,5}): 6,
#     frozenset({8,9}): 10
# }

# print(dict)
## pratical example 
## use a dictionary to count he frequency of element in list

numbers =[1,2,3,3,3,4,4,4,4]
frequency ={}

for i in numbers:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1 
print(frequency)        

