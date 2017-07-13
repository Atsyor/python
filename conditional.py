i = 8
if(i % 3):
	print "Odd Number"
else:
	print "Even Number"
 
 
def get_age():
    age = (int)(raw_input("whats your age? "))
    if(age <12):
        print "you are a child"
    elif(age < 20):
        print "you are young"
    elif(age < 46):
        print "you are old"        

get_age()





num = [1,2,3,4,5,6,7,8,9,10,11,12]
result = 0
for item in num:
    
    if not item%2:
             result += item        

print result




    
