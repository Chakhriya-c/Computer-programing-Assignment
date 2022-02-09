#GPA = credit * Grade / totalcredit

sys_grade= {"A":4,"B+":3.5,"B":3.0, "C+":2.5,"C":2.0, "D+":1.5, "D":1.0,"F":0} #initial grade system

print ("How many subject you enrolled?")                            #collect number of subject
number_of_subject = int(input())

total_grade = 0     #initial user's total grade
total_credit = 0    #initial user's total credit

for n in range(number_of_subject):
    user_grade = 0                                                  #initial user's grade by subject 
    print ("Enter Subject number " + str(n+1) + " 's Credit: ")     #collect user's credit by subject
    user_credit = int(input())
    print ("Enter your Grade: ")                                    #collect user's grade by subject
    user_grade = str(input())
    
    subject_grade = sys_grade[user_grade] * user_credit             #calculate user's grade by subject

    total_grade += subject_grade                                    #storing user's grade by subject
    total_credit += user_credit                                     #storing user's credit by subject

    gpa = total_grade / total_credit                                #calculate and store user gpa

print ("Total Credit = " + str(total_credit))                       #output of Total Credit
print("GPA = " + str(gpa))                                          #output of User's GPA

    






