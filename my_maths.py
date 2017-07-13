def calculate(op1, op2, f):
    if f == "add":
        return op1 + op2
		
    elif f == "subtract":
        return op1 - op2
			
    elif f == "divide":
		return op1 / op2
				
    elif f== "multiplication":
		return op1 * op2

result = calculate(2,7, "add")
print result


# if have to be in the same line with elif 
# return must also be in the same line 
#the function must be in the string eg"add", "subtract" and two into argument eg (2,7) ,(3,4)
#for the function to run it need to take an argument eg print result than press f5 for it to run 
#the end

