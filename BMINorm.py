def calculate ( x, y):
    if (x<=0 or y<=0):
        print("|\tInvalid Category.\t\t|\n|   Check Your Height and Weight\t|")
    else:
        BMI =( y/(x**2))
        BMI = round(BMI,2)
        print("|\tYour BMI Value is ",BMI,"\t|")
        print("|\tYour category :\t\t|")
        if (BMI <18.5):
            print("|\t   Under Weight\t\t|")
        elif(BMI<= 24.9):
            print("|\t   Normal Weight\t\t|")
        elif(BMI<= 29.9):
            print("|\t   Over Weight\t\t|")
        else:
            print("|\t   Obese\t\t\t|")
n= int(input("Enter the count of members : "))
for i in range(1, n+1):
    print("Member : ",i)
    a = input("Enter your Name : ")
    b= float(input("Enter your height (in meters) : \n"))
    c= float(input("Enter your weight (in kilogram): \n"))
    print(" ----***---BMI REPORT---***---- ")
    print("|                                    \t\t|")
    print(f"|\tYour Name is {a}\t|")
    print(f"|\tYour Weight is {c} KG\t|")
    print(f"|\tYour Height is {b} meters\t|")
    calculate(b,c)
    print("|                                    \t\t|")
    print("-----------------------------------------")


