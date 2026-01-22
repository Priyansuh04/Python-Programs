

##### Assignment 10: Tuple and List

##Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, 
# and convert it back to a tuple. Print the resulting tuple.

tpl = (1,2,3,4,5)
lst =list(tpl)
lst.append(6)
tcl =tuple(lst)
print(tcl)