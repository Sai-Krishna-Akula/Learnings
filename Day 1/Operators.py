# sum  +
# sub  - 
# Mul  *
# Div  //
# Remainder %


# sum of two numbers  
# inputs are static values
a = 10
b = 30
print("Sum of two numbers ", a+b)


# subtraction of two numbers
# inputs are static values
a = 10
b = 30
print(f"{b}-{a}={b-a}")

# multipliaction of two numbers
# Dynamic inputs using the input method
a = int(input('Enter value a = '))
b = int(input('Enter value b = '))
print(f"{a}*{b}={a*b}")

# Division
# Dynamic inputs using the input method
print(f"{a}/{b}={a/b}")

# quotient and remainder of two numbers
print(f"Quotient of {a} and {b} is {a//b}")
print(f"Remainder of {a} and {b} is {a%b}")