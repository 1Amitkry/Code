def add (num1,num2):
    return num1+num2

def subtract (num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    if num2 == 0:
        return ("Error")
    else:
        return num1/num2

def modulus(num1,num2):
    return num1%num2

def exponent(num1,num2):
    return num1**num2

def floor_division(num1,num2):
    return num1//num2


operations= {
"+" : add,
"-" :subtract,
"*" :multiply,
"/" :divide,
"%" : modulus,
"**" : exponent
}


def calculator():
    #should_accumulate = True
    num1 = float(input("Enter first number: "))

    while True:
            
        num2 = float(input("Enter next number: "))
        try:  
            for symbol in (operations):
                print(symbol)

            operation = input("select operation:")

            if operation == "+":
                answer = add(num1,num2) 
                print(f'{num1} {operation} {num2} = {answer}')
            elif operation == "-":
                answer = subtract(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}')
            elif operation == "*":
                answer = multiply(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}' )
            elif operation == "/":
                answer = divide(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}' )

            elif operation == "%":
                answer = modulus(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}' )

            elif operation == "**":
                answer = exponent(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}' )
            
            elif operation == "//":
                answer = floor_division(num1,num2)
                print(f'{num1} {operation} {num2} = {answer}' )
            else:
                print("Invalid input")
        except:
            print("Select operation")

        choice = input(" If you want to continue with previous Type 'y' : \n if you want to start new Type 'n' : \n if you want to stop type 'e' :")

        if choice == "y":
            num1 = answer
    
        elif choice == 'n':
            should_accumulate = False
            #print("Thankyou!!!")
            calculator()
        else:
            print("Thank you for using calculator!!!")
            break
calculator()
