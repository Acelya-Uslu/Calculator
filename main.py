number1= int(input("First number:"))
number2= int(input("Second number:"))

operation=input("Bir işlem seçiniz(+,-,/,*):")


if operation== "+":
    print(number1,"+",number2,"=",number1+number2)

elif operation=="-":
    print(number1,"-",number2,"=",number1-number2)


elif operation=="*":
    print(number1,"*",number2,"=",number1*number2)


elif operation =="/":
    print(number1,"/",number2,"=",number1/number2)
else:
    print("Invalid operation.Please try again.")