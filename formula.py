# write program to calculate formulas
# User will provide all inputs
# area and perimeter of circle
# area and perimeter of rectangle
# area and perimeter of triangle
# volume and surface area of sphere
# volume and surface area of cylinder




shape = input("Enter shape: Rectangle,Square,Circle,Triangle,Cylinder,cone::").lower().title()


#Rectangle
if shape == "Rectangle":          
    while True: 
        try:
            length = float(input("Enter length of Rectangle in cm: "))           #float type because the values  could be in decimals
            break
        except:
            print("Enter Valid value!")
    while True:
        try:
            breadth = float(input("Enter breadth of rectangle in cm: "))
            break
        except:
            print("Enter valid input!")
             #Want it to be such that if the user inputs something differnt than numbers it shows error and give them warning and again give them chance of entering an interger value 
    operation = input("You want area/perimeter ?")
    
    if operation == "Area".lower().title():
            print("Area is " + str(length*breadth) + " cm sq")                  #str(length*breadth) because the carcation take place in same type "Area is" this is a string value so the other must be converted to  string or vice versa.
    elif operation == "Perimeter".lower().title():
                print("Perimeter is : " + str(2*(length+breadth)) + "cm")
    else:
        print("Choose correct option/Check Spelling!")





 #Square        
elif shape == "Square":
    while True:
        try:
            side = float(input("Enter side of square in cm :"))
            break
        except:
            print("Enter a valid value!")
    

    operation = input("You want Area/Perimeter? ")
    if operation == "Area".lower():
        print("Area of square is " + str(side*side) + " cm sq")
    elif operation == "Perimeter":
        print("Perimeter of square is " +str(4*side) + " cm")
    else:
        print("Choose correct option/check spelling!")

    


 #circle
elif shape == "Circle":
    while True:
        try:
            radius = float(input("Enter Radius in cm:")) #Taking radius as float in place of integer as radius can be in decimal
            break
        except:
            print("Enter valid input!")

    operation = input("You want Area/Circumference ?")
    if operation == "Circumference".lower():
        print("Circumference of circle is: " + str(2*3.14*radius) + " cm")
    elif operation == "Area".lower():
        print("Area of circle is: " + str(3.24 *radius *radius) + " cm sq.")
    else:
        print("Select correct option/check spelling!")



 #Triangle
elif shape == "Triangle":
    operation = input("You want Area/Perimeter? ")
    if operation == "Area".lower():
        Base = float(input("What is base of the triangle  in cm ? "))
        Height = float(input("What is the Height of the triangle in cm ? "))
        print("Area of the triangle is " + str(0.5*Base*Height) + " cm sq")
    elif operation == "Perimeter".lower():
        A = float(input("Enter length of side A in cm : "))
        B = float(input("Enter length of side B in cm : "))
        C = float(input("Enter length of side c in cm : "))
        Perimeter =float(A+B+C)
        print("Perimeter is " + str(Perimeter) +" cm")
    else:
        print("Enter correct value ")


#Cylinder
elif shape == "Cylinder":
    while True:
        try:
            Radius = float(input("Enter radius in cm : "))
            break
        except:
            print("Enter valid numbers: ")
    while True:
        try:
            Height =float(input("Enter Height in cm: "))
            break
        except:
            print("Enter valid numbers: ")

    operation = input("You want to calculate Volume/TSA/CSA : ")
    if operation == "volume".lower():
        print("Voulume of Cylinder is : " + str(3.14*Radius*Radius*Height) + " cm cube")
    elif operation == "CSA".lower():
        print("Curved surface area of cylinder is :" +str(2*3.14*Radius*Height) + " cm sq")
    elif operation == "TSA".lower():
        print("Total surface area of the cylinder is : " + str(2*3.13*Radius*(Radius+Height)) + " cm sq")
    else:
        print("Select correct operation ")
    
            
else:
    print("Try Again!")





