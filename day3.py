#boolean , list


# var1 = True
# var2 = False
# print(var1, var2)
# print(type(var1), type(var2))   #in boolean we can only store true or false value
# in boolean firsst letter of true and false is always capital

#array = collection of similar datatype


# python list = is a alternative of array  
# can store any datatype non similar also
# no fixed size [dynamic nature]

# types of array
# 1. static = fixed size and similar data type
# 2. dynamic = not fixed but similar data type
# 3. referential = can store non similar datatype
  


# how to create list in python
# ls = [25,41,36,4,25.2,21.,30.1, "upflair",True]
# print (ls)
# print(type(ls))


# ls = [10,12,13,14,15,16]
# print(ls[-5])


# ls = [5,10,13,14,"upflairs",100]
# var = ls[4]
# print(var[4:7])
  


student_name = ["taniya","yash","prerna","ruchika","aditya","kalika"]
# student_name[0] = "tanya" #manupluation or updation
# print(student_name)
# student_name.append("jugnu") 
# student_name.append('ritu') #append is used to enter new data or to insert at last
# print(student_name)

# student_name.pop()
# print(student_name)  # pop remove the item from the last position


# student_name.insert(1,"gurpreet") 
# student_name.remove("prerna")
# del student_name[2]
# print(student_name)
# print(student_name.count("yash"))

# ls1 =['A','B','C','D','E']
# ls2 = [85,4,5,6,9,85,25,4,63,6,7]

#LS1.REVERSE() #LS1[::-1]

# ls2.sort()    #assending order
# print(ls2[::-1]) # decending order


# print(min(ls2))
# print(max(ls2))
# print(sum(ls2))
# # ls1.clear()
# print(ls1.index('C'))


# ls2 = [10,20,3.1, 'upflair pvt ltd', 500,400]

# ls2 [2] = 100
# print(ls2)

# ls2[3] = "flipkart pvt ltd"
# print(ls2)



# >>>>>>>>>>>>>>>>>>>TUPLE<<<<<<<<<<<<<<<<<<<<<<<<
#unchangable



# tpl = (25,41,6396,"upflairs",True,25.2)
# print(tpl)
# print(type(tpl))

# tpl[4] = "flipkart"
# print(tpl)



# <<<<<<<<<<<<<<<<<<<SET<<<<<<<<<<<<<<<<<<<<<<<<

# st = {52,1,63,85,74,96,54,74,96,54,25,45,8,54,5,66,3,54}
# print(st)
# print(type(st))



# <<<<<<<<<<<<<<<<<<<<<<<<<<<DICTIONARY>>>>>>>>>>>>>>>>>>>>>>>>>>
# marks = {"mohit":52,"rohit":53, "rocky":56,"mohit":54}
# print(marks)
# print(type(marks))