from math import floor 
import math
from datetime import datetime 
import pprint

# firstname = "koohyar"
# lastname= "noroozi"
# age= 13



# a = 23
# b = 34

# print( a + b)
# print(b * a)
# print(a* b / 2)

# niloufar = {
#   "f.name":"nioofar", 
#   "l.name" : "Ramezani" , 
#   "age" : 30 , 
#   "career" : "Full Stack" , 
#   "TM" : " 1000",


# }
# print(niloufar["f.name"])
# print(niloufar["l.name"] , niloufar["age"])
# print(niloufar["career" ],niloufar ["TM"] )

# tm = int(niloufar["TM"])
# print( tm / 30)

# mahsool = [
#     {"name" :"boliz" , "price" : "120"},
#     {"name" : "shalvr" , "price" : "170"}
# ]

# print(mahsool[0])

# her = ("sima" , "shabani")
# print(her)




# help(dict)
# help(tuple)


# age = input("when is your birth age?")
# print(2024 - int(age))

# niloufar = []
# name = input("what's your name?")
# niloufar.append(name)
# print(niloufar)

# print(floor(5.9))
# print(datetime.year)

# file = open("message.txt" , "w" , encoding ="utf-8")
# file.write("hello\n")
# file.write("close\n")
# file.close()


# file = open("message.txt" , "r" , encoding="utf-8")
# content = file.read()

# print(content)
# username = input("Username:")
# password = input("Password:")

# with open("username.txt" , "w" , encoding="utf-8") as file:
#     file.write(username +"\n")
#     file.write(password + "\n")
#     file.close()


# with open("username.txt" , "r" , encoding="utf-8") as file:
#     content = file.read()

# print(content)





# todo list :

# todolist = []
# txt= input("what's your routine? \n")
# todolist.append(txt)
# print("Did you " + txt + "?")

# if txt :
#     with open("todolist" , "w" , encoding="utf-8") as  file:
#         file.write(txt + "\n")
#         file.close()
#     with open("todolist" , "w" , encoding="utf-8") as  file:
#         content = file.read()
# else:
#     print("you should write sth")
     
# print(content)
# print(todolist)

#  example 1:
# a = input("name \n")
# b = input("family \n")
# c= input("years \n")
# d=input("average")


# students =[]
 
# first_student = {
#     "name" : a ,
#     "family" : b ,
#     "years": c,
#     "average" : d,
# }

# second_student = {
#     "name" : a ,
#     "family" : b ,
#     "years": c,
#     "average" : d,
# }
# third_student ={
#       "name" : a ,
#     "family" : b ,
#     "years": c,
#     "average" : d,
# }


# students.append([first_student])
# students.append([second_student])
# students.append([third_student])

# with open("first_student" , "w" , encoding="utf-8") as file:
#     file.write(first_student["name"]+ "\n")
#     file.write(first_student["family"]+ "\n")
#     file.write(first_student["years"]+ "\n")
#     file.write(first_student["average"]+ "\n")
#     file.close()

# with open("first_student" , "r" , encoding="utf-8") as file:
#     content = file.read()

# with open("second_student" , "w" , encoding="utf-8") as file:
#     file.write(first_student["name"]+ "\n")
#     file.write(first_student["family"]+ "\n")
#     file.write(first_student["years"]+ "\n")
#     file.write(first_student["average"]+ "\n")
#     file.close()

# with open("second_student" , "r" , encoding="utf-8") as file:
#     content = file.read()

# with open("third_student" , "w" , encoding="utf-8") as file:
#     file.write(first_student["name"]+ "\n")
#     file.write(first_student["family"]+ "\n")
#     file.write(first_student["years"]+ "\n")
#     file.write(first_student["average"]+ "\n")
#     file.close()

# with open("third_student" , "r" , encoding="utf-8") as file:
#     content = file.read()


# print(a)
# print(b)
# print(c)
# print(students)
# print(content)
# name ="john"
# message1 = f"Hello, {name}!"
# print(message1)

# students = []
# first_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# first_student["name"] = fname
# first_student["Last name"] = lname
# first_student["Birth_year"]= birth_year
# first_student["average"]= average

# students.append(first_student)



# second_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# second_student["name"] = fname
# second_student["Last name"] = lname
# second_student["Birth_year"]= birth_year
# second_student["average"]= average

# students.append(second_student)
# print(second_student["name"] + second_student ["Last name"])

# third_student = {}
# fname = input("First Name")
# lname = input("Last Name")
# birth_year = int(input("Birth Year"))
# average = float(input("average"))

# third_student["name"] = fname
# third_student["Last name"] = lname
# third_student["Birth_year"]= birth_year
# third_student["average"]= average

# students.append(third_student)
# print(third_student["name"] + third_student ["Last name"])


# pprint.pprint(students)

# # upper() and  " "
# uperName = students[0]
# first_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(first_upeper_name.upper())

# uperName = students[1]
# second_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(second_upeper_name.upper())

# uperName = students[2]
# third_upeper_name = (uperName["name"]) + " " + uperName["Last name"]
# print(third_upeper_name.upper())


# # average 
# mark = students[0]
# first_mark = mark["average"]

# mark = students[1]
# second_mark = mark["average"]

# mark = students[2]
# third_mark = mark["average"]


# average_of_three = (first_mark + second_mark + third_mark)/3 
# print(floor(average_of_three))

# a = 2
# b = 5

# print(a == b )
# print(a != b )
# print(a < b )
# print(a > b )
# print(a >= b )
 


# a =["mamad" , "ali" , "kia"]

# for i in a:
#     print(i)


# first_name = input("what's your name?")
# last_name = input("what's your last name?")
# birth_year = int(input("tell me about your birth yaer"))
# gpa = float(input("what is your GPA"))
# count = 3

index = 0
students = [ 
    # {"name" : first_name , "last_name" : last_name , "birth_year" : birth_year , "gpa" : gpa} 
    ]

for i in range(3):

    first_name = input("what's your name?")
    last_name = input("what's your last name?")
    birth_year = int(input("tell me about your birth yaer"))
    gpa = float(input("what is your GPA" ))

    student= {
        "name" : first_name ,
        "family" : last_name , 
        "birth_year" : birth_year ,
        "gpa" : gpa
    }

    students.append(student)

average = 0
while index < 3 :
        id = students[index]["name"] + " " + students[index]["family"]
        gpa_of_three = students[index]["gpa"]
        average = average + gpa_of_three
        index += 1
        pprint.pprint(id.upper())
        print(average)

pprint.pprint(students)
print(average / len(students))


   

