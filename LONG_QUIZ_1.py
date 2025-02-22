def get_valid_score(prompt):
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100: 
                return score
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def convert_to_ucc_grade(final_grade):
    if 99 <= final_grade <= 100:
        return 1.00
    elif 95 <= final_grade <= 98:
        return 1.25
    elif 90 <= final_grade <= 94:
        return 1.50
    elif 85 <= final_grade <= 89:
        return 1.75
    elif 80 <= final_grade <= 84:
        return 2.00
    elif 75 <= final_grade <= 79:
        return 2.25
    elif 70 <= final_grade <= 74:
        return 2.50
    elif 65 <= final_grade <= 69:
        return 2.75
    elif 60 <= final_grade <= 64:
        return 3.00
    else:
        return 5.00

def enroll_in_course():

    course_name = "CPE103"
    confirmation = input(f"Enroll in {course_name}? (yes/no): ").strip().lower()
    return confirmation == "yes"

print("Student's Information")
print()
name = input("Enter Student's Name: ")
student_id = input("Enter Student's ID: ")
program = input("Enter Student's Program: ")
sex = input("Student's Sex: ")
weight = float(input("Enter Student's weight(in kg): "))
height = float(input("Enter Student's height(in cm): "))


if not enroll_in_course():
    print("You must enroll in the course to proceed.")
else:
    print("Successfully enrolled in CPE103.")
    print()

    MHOS = get_valid_score("Enter Midterm Hands-on Seatwork grade: ")
    MQUIZ = get_valid_score("Enter Midterm Quiz grade: ")
    MAS = get_valid_score("Enter Midterm Assignment grade: ")
    MCS = MHOS * 0.5 + MQUIZ * 0.3 + MAS * 0.2
    print("Midterm CS is: ", MCS)
    MEX = get_valid_score("Enter Midterm Exam grade: ")
    MG = MEX * 0.5 + MCS * 0.5
    print("Midterm Grade is: ", "%.2f" % MG)

    print()

    FHOS = get_valid_score("Enter Finals Hands-on Seatwork grade: ")
    FQUIZ = get_valid_score("Enter Finals Quiz grade: ")
    FAS = get_valid_score("Enter Finals Assignment grade: ")
    FCS = FHOS * 0.5 + FQUIZ * 0.3 + FAS * 0.2
    print("Finals CS is: ", FCS)
    FEX = get_valid_score("Enter Finals Exam grade: ")
    FG = FEX * 0.5 + FCS * 0.5
    print("Finals Grade is: ", "%.2f" % FG)

    ucc_grade = convert_to_ucc_grade(FG)
    print("UCC Numerical Grade: ", ucc_grade)
