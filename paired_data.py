def student_courses(student_name):
    """This function loops over paired data to check for courses a student 
    hass registered for"""

    count = 0
    students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

    for i,j in students:
        if i == student_name:
            for i in j:
                print(i)
                count += 1
    if count == 0:
        print(f"{student_name} has not registered for any courses")
    else:
        print(f"{student_name} has registered for {count} courses")

student_name = input("Enter the name of the student: ")
student_courses(student_name)
