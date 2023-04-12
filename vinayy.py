print='''
+ add
- subtract
* multiple
/ divide
'''
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
oper=input("enter operator:")
if oper=="+":
  print(num1+num2)
elif oper=="-":
  print(num1-num2)
elif oper=="*":
  print(num1*num2)
elif oper=="/":
  print(num1/num2)
else:
    print("invalid number")






