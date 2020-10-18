# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:02:44 2020
Error handling for student grade assignment
@author: Ashish
"""
data_valid = False
grade1 = float(input("Type the grade of the first test: "))
grade2 = float(input("Type the grade of the second test: "))
absences = int(input("Type the number of absences: "))
total_classes = int(input("Type the total number of classes: "))

avg_grade = (grade1+grade2)/2
attendance = (total_classes-absences)/total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance Rate: ", str(round(attendance*100,2))+"%")

if avg_grade>=6 and attendance >=0.8:
    print("The student is approved")
elif avg_grade<6 and attendance <0.8:
    print("The student has failed due to an avg grade lower than 0.6 and attandance lower than 0.8")
elif attendance >=0.8:
    print("The student has failed due to an average grade lower than 6.0")
else:
    print("The student has failed due to attendance rate lower than 80%")
