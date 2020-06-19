
name = input("What is your name")
print(name)
yob = input("What is your birth year?")
print(type(yob))
age = 2020 - int(yob)
print(age)

course = "Python"
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print(course[-1:3])
print(course[0:-3])
print(course[-3:])
print(len(course))


student_name = "Yogesh"
student_age = 19
is_student = True
print(type(student_name))
print(type(student_age))
print(type(is_student))

#name = input("What is your name: ")
print(name)
food = input("What is your favourite food?: ")
print(name + " likes " + food)

temp_celsius = input("Enter temperature in celsius: ")
temp_f = (float(temp_celsius) * 9/5)+32
print("Temperature in Fahrenheit = " + str(temp_f))

#Fullname = input("Enter your full name: ")
print(name.title())

