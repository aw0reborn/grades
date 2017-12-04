## IMPORTS GO HERE

## END OF IMPORTS

#### YOUR CODE FOR get_grade() FUNCTION GOES HERE ####
def get_grade(x):
    x=int(round(x))
    if (x >= 0) and (x<50):
        return'F'
    elif (x >= 50) and (x<54):
        return'D'
    elif (x>=54) and (x<58):
        return'D+'
    elif (x>=58) and (x<62):
        return'C-'
    elif(x>=62) and (x<66):
        return'C'
    elif(x>=66) and (x<70):
        return'C+'
    elif(x>=70) and (x<74):
        return'B-'
    elif(x>=74) and (x<78):
        return'B'
    elif(x>=78) and (x<82):
        return'B+'
    elif(x>=82) and (x<86):
        return'A-'
    elif(x>=86) and (x<90):
        return'A'
    elif(x>=90) and (x<=100):
        return'A+'
    else:
        return None 
#### End OF MARKER

#### YOUR CODE FOR calculate_sgpa() FUNCTION GOES HERE ####
def calculate_sgpa(grade1=0,grade2=0,grade3=0):
    total_marks=0
    total_number_of_subjects=0
    
  
    if grade1 != 'nothing' :
        total_number_of_subjects += 1
        if grade1=="A+":
            total_marks+=4.0
        if grade1=="A":
            total_marks+=4.0
        if grade1=="A-":
            total_marks+=3.67
        if grade1=="B+":
            total_marks+=3.33
        if grade1=="B":
            total_marks+=3.0
        if grade1=="B-":
            total_marks+=2.67
        if grade1=="C+":
            total_marks+=2.33
        if grade1=="C":
            total_marks+=2.0
        if grade1=="C-":
            total_marks+=1.67
        if grade1=="D+":
            total_marks+=1.33
        if grade1=="D":
            total_marks+=1.0
        if grade1=="F":
            total_marks+=0.0
    if grade2 != 'nothing' :
        total_number_of_subjects += 1
        if grade2=="A+":
            total_marks+=4.0
        if grade2=="A":
            total_marks+=4.0
        if grade2=="A-":
            total_marks+=3.67
        if grade2=="B+":
            total_marks+=3.33
        if grade2=="B":
            total_marks+=3.0
        if grade2=="B-":
            total_marks+=2.67
        if grade2=="C+":
            total_marks+=2.33
        if grade2=="C":
            total_marks+=2.0
        if grade2=="C-":
            total_marks+=1.67
        if grade2=="D+":
            total_marks+=1.33
        if grade2=="D":
            total_marks+=1.0
        if grade2=="F":
            total_marks+=0.0
        
       
    if grade3 != 'nothing' :
        total_number_of_subjects += 1
        if grade3=="A+":
            total_marks+=4.0
        if grade3=="A":
            total_marks+=4.0
        if grade3=="A-":
            total_marks+=3.67
        if grade3=="B+":
            total_marks+=3.33
        if grade3=="B":
            total_marks+=3.0
        if grade3=="B-":
            total_marks+=2.67
        if grade3=="C+":
            total_marks+=2.33
        if grade3=="C":
            total_marks+=2.0
        if grade3=="C-":
            total_marks+=1.67
        if grade3=="D+":
            total_marks+=1.33
        if grade3=="D":
            total_marks+=1.0
        if grade3=="F":
            total_marks+=0.0
       
    if total_number_of_subjects== 0:
        return 0
    else:
        sgpa = total_marks/total_number_of_subjects
        return sgpa
#### End OF MARKER

