def interest():
    principal = float(input("principal amount"))
    apr = float(input("annual Interest reate <value must between 0.0 and 1.0>"))
    if not (0.0 <= apr and apr <= 1.0):
        print("Error")
        return False
    final = principal
    for i in range(10.0):
        final *= (1+apr)
    print("The final amount after 10 years is ", final)


def factorial():
    fact = 1
    for num in [6,5,4,3,2,1]:
        fact *= num
        print("", fact)

def quad():
    print("This function returns the roots of the quadratic equation")
    a = float(input("plz input the coefficient 'a'"))
    b = float(input("plz input the coefficient 'b'"))
    c = float(input("plz input the coefficient 'c'"))
    if b**2 - 4 * a * c < 0:
        print("No Realnumber Root")
        return False
    root1 = (-b - pow(b**2 - 4 * a * c,0.5))/(2 * a)
    root2 = (-b + pow(b**2 - 4 * a * c,0.5))/(2 * a)
    print("Root 1 is : ", root1)
    print("Root 2 is : ", root2)

quad()