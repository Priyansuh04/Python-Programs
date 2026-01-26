

##### Assignment 10: Tuple and List

##Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, 
# and convert it back to a tuple. Print the resulting tuple.

# tpl = (1,2,3,4,5)
# lst =list(tpl)
# lst.append(6)
# tcl =tuple(lst)
# print(tcl)

## Organizing student grades 
grades =[85,92,78,98,88]

## Adding a new grades 
grades.append(95)

## Calculating the average grades 
average_grades = sum(grades) / len(grades)
print(f"Average Grades: {average_grades:.2f}")

## Finding the highest and lowest grades 
highest_grades =max(grades)
lower_grades =min(grades)
print(f"Highest Grades: {highest_grades}")
print(f"Lower_Grades: {lower_grades}")
 