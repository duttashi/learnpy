# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:37:16 2020

@author: Ashish

Use the logic for assigning grade to student defined in
assign_grade_to_student_using_function.py script.
The idea is to create a class with a constructor to initialise
relevant variables like student exam related data from the user,
roll number, test mark, exam mark etc.
It will then pass this data as argument into another function.
The other function will pull the data out of the arguments
and use them for further analysis.

Note: the __init__() is a constructor to initialise variables

"""

student_info_list = []


class GradeAssigner:

    def __init__(self):
        print("The init is called")
        # self.test_mark = test_mark
        # self.tut_mark = tut_mark
        # self.exam_mark = exam_mark

    def get_student_details(self):
        stud_num = input("Enter the student number: ")
        stud_tutorial_mark = float(input("Enter student's tutorial mark:"))
        stud_test_mark = float(input("Enter student's test mark:"))
        stud_exam_mark = float(input("Enter student exam mark: "))
        # add data to list
        student_info_list.append(stud_num)
        student_info_list.append(stud_tutorial_mark)
        student_info_list.append(stud_test_mark)
        student_info_list.append(stud_exam_mark)
    # return a list of items
        return student_info_list

    def calculate_grade(self, student_info_list):
        stud_num = student_info_list[0]
        stud_test_mark = student_info_list[1]
        stud_tutorial_mark = student_info_list[2]
        stud_exam_mark = student_info_list[3]
        if stud_tutorial_mark+stud_test_mark/2 < 40:
            grade = "Fail"
        final_mark = (stud_tutorial_mark+stud_test_mark+2*stud_exam_mark)/4
        if 80 <= final_mark <= 100:
            grade = "A"
        elif 70 <= final_mark < 80:
            grade = "B"
        elif 60 <= final_mark < 70:
            grade = "C"
        elif 50 <= final_mark < 60:
            grade = "D"
        else:
            grade = "E"
        return stud_num, final_mark, grade


# student = GradeAssigner()  # create an object of the class
student = GradeAssigner()
get_student_info = student.get_student_details()
snum, fmark, grade = student.calculate_grade(get_student_info)
print("student %s's final mark is %d and grade is %s." % (snum, fmark, grade))
