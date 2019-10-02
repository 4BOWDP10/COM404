print ("please enter the first whole number")
first = int(input())
print ("please enter the second whole number")
second = int(input())
print ("please enter the third number")
third = int(input())

evenTally = 0
oddTally = 0

if first % 2 == 0:
    evenTally = evenTally + 1
else:
    oddTally +=1    
if second % 2 == 0:
    evenTally = evenTally + 1
else:
    oddTally +=1    
if third % 2 == 0:
    evenTally = evenTally + 1
else:
    oddTally +=1    

print ("even numbers"+ str(evenTally))
print ("odd numbers"+ str(oddTally))
