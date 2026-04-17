from collections import namedtuple


def average_namedtuple(students, columns):
    student = namedtuple('std',columns)
    no_of_students=len(students)
    total_marks=0
    for details in students:
        s11=details.split()
        s=student(s11[0],s11[1],s11[2],s11[3])
        total_marks=total_marks+int(s.MARKS)

    average=total_marks/no_of_students
    return average

if __name__=="__main__":
    students=["21 77 Ramond 97","16 9 Raymon 67","13 98 Raymod 73","11 99 Raymnd 4","3 96 Rymond 8"]
    columns= "ID MARKS NAME CLASS" 
    class_average=average_namedtuple(students,columns)
    print(class_average)