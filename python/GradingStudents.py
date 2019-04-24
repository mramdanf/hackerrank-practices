import math

def gradingStudents(grades):
    #
    # Write your code here.
    #
    result = []
    for grade in grades:
        nextFive = (math.ceil(grade/5)) * 5 if grade%5 != 0 else grade + 5
        diff     = nextFive-grade
        
        if grade < 38 or diff == 3: 
            result.append(grade)
        else: 
            result.append(nextFive)
    
    return result

if __name__ == '__main__':
    grades = [75, 75, 75]
    # nextFive [75, 70, 40, 35]
    # diff     [2, 3, 2, 2]
    # result   [75, 70]
    print (gradingStudents(grades))