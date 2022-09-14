# 1. Write a python script to take your name as input from the user and then print it.
name = input("Enter your name.\n")
print("My name is", name)
print()

# 2. Write a python script to take input from the user. Input must be a number.
num = float(input("Enter any number\n"))
print("You enter  ", num)
print()

# 3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
num1 = float(input("Enter number 1\n"))
num2 = float(input("Enter number 2\n"))
print("Sum of ", num1, " and ", num2, "is ", num1+num2)
print()
# 4. Write a python script which takes the radius from the user and display area of a circle.
radius = float(input("Enter the radius...\n"))
area = 3.14*radius*radius
print("The area", "of", radius, "is ", area)
print()

# 5. Write a python script to calculate the square of a number. Number is entered by the user.
num = float(input("Enter number 1\t"))
print("Square of ", num, "is ", num**2)
print()

# 6. Write a python script to calculate the area of Triangle. Number is entered by the user.
len = float(input("Enter lenth of traingle\n"))
height = float(input("Enter height of triangle\n"))
Area = 1/2*(len*height)
print("Area of traingle of length = ", len, "and height = ", height, "= ", Area)
print()

# 7. Write a python script to calculate average of three numbers, entered by the user
num1 = float(input("Enter num1\t"))
num2 = float(input("Enter num2\t"))
num3 = float(input("Enter num3\t"))
avg = (num1+num2+num3)/3
print("Average of ", num1, ",", num2, "and", num3, "is", avg)
print()

# 8. Write a python script to calculate simple interest
p = float(input("Enter principal\t"))
t = float(input("Enter time period "))
r = int(input("Enter rate of interest\t"))
print('The principal is', p)
print('The time period is', t)
print('The rate of interest is', r)
si = (p * t * r)/100
print('The Simple Interest is', si)
print()

# 9. Write a python script to calculate the volume of a cuboid.
len = int(input("Enter length of cuboid\t"))
height = int(input("Enter height of cuboid\t"))
width = int(input("Enter width of cuboid"))
volume = len*height*width
print("Volume of cuboid of length= ", len, ",height= ",height, "and width= ", width, "is ", volume)
print()

# 10. Write a python script to calculate area of a rectangle
len = int(input("Enter length of rectangle\t"))
width = int(input("Enter width of rectangle\t"))
print("Area of rectangle of length ", len,"and width ", width, "is ", len*width)
