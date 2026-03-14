a = input("Enter your Name : ")
b= float(input("Enter your height (in meters) : \n"))
c= float(input("Enter your weight (in kilogram): \n"))
if (b<=0 and c==0):
    print("Invalid Input ")
else:
  BMI =float( c/(b**2))
  print("Your Name is ",a)
  print("Your Weight is ",c,"KG")
  print("Your Height is ",b,"meters")
  print(" ----***---BMI REPORT---***---- ")
  print("|                                    \t\t|")
  print(f"|\tYour Name is {a}\t|")
  print(f"|\tYour Weight is {c} KG\t|")
  print(f"|\tYour Height is {b} meters\t|")
  print("|\tYour BMI Value is ",round(BMI,2),"\t|")
  print("|\tYour category :\t\t|")
  if (BMI <18.5):
            print("|\t   Under Weight\t\t|")
  elif(BMI<= 24.9):
            print("|\t   Normal Weight\t\t|")
  elif(BMI<= 29.9):
            print("|\t   Over Weight\t\t|")
  else:
            print("|\t   Obese\t\t\t|")
  print("|                                    \t\t|")
  print("-----------------------------------------")






            
