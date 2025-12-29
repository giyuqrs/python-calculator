num1 = float(input("pehla number dalo:  "))
num2 = float(input("dusra number dalo: "))

print ("operations:")
print("+  Addition ")
print("-  subtraction")
print("*  Multiplication")
print("/  Divison")


op = input("Operation choose karo (+, -, *, / ):  ")

if op == "+":
	print("Result:", num1+ num2 )
	
elif op == "-":
	print("Result:", num1 - num2)	
	
elif op == "*":
		print("Result:", num1 * num2)
		
elif op == "*":
    	print("Result:", num1 * num2)
    	
elif op == "/":
    	if num2 != 0:
    		print("Result:", num1 / num2) 
    	else:
    		print("Error: 0 se divide nahi hota")
     
else:
  		print("Invalid operation")