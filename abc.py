PI = 3.14
radius = float(input("Enter the radius"))
print(radius)
area = PI * radius * radius
print(area)


# WAP to accept a filename from the user and print the extension of that:

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
