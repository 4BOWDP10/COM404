# Read in user data 
print("What is your name?")
name = input() 

print("What is your age?")
age = int(input())

print("What is your weight? In Kilos") 
weight = float(input()) 

print("What is your height? In Meters, i.e 1.73")
height = float(input())

# Calculate bmi
bmi = weight / (height ** 2)

# Display result
print(name, "your bmi is", bmi)
