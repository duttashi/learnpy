# write a program to calculate the body mass index (bmi) of a person
# accept the height and weight of a person
# BMI = weight/(height * weight)
# Print the BMI based on following conditions:
# less than or equal to 18.5: print underweight
# greater than 18.9 or less then 24.9: print normal weight
# greater than 24.9 or less then 29.9: print overweight
# greater than or equal to 30: print obesity

weight = float(input("Enter weight: "))
height = float(input("Enter height: "))
bmi = weight/(height*weight)
if(bmi<=18.5):
    print("You are underweight")
elif(bmi>18.9 and bmi<24.9):
    print("You have a normal weight")
elif(bmi>24.9 and bmi<29.9):
    print("You are overweight")
else:
    print("You are obese!")