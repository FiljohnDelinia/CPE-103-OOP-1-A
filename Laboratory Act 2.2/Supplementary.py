# Student Name Input
name = input("Enter student name: ")
print("\nEnter all grades out of 100")

# PRELIM INPUT
hoa1 = float(input("Prelim Hands-on average: "))
quiz1 = float(input("Prelim Quiz average: "))
assign1 = float(input("Prelim Assignment average: "))
exam1 = float(input("Prelim Exam: "))

# MIDTERM INPUT
hoa2 = float(input("Midterm Hands-on average: "))
quiz2 = float(input("Midterm Quiz average: "))
assign2 = float(input("Midterm Assignment average: "))
exam2 = float(input("Midterm Exam: "))

# FINAL INPUT
hoa3 = float(input("Final Hands-on average: "))
quiz3 = float(input("Final Quiz average: "))
assign3 = float(input("Final Assignment average: "))
exam3 = float(input("Final Exam: "))

# PRELIM CALCULATION
cs1 = 0.5 * hoa1 + 0.3 * quiz1 + 0.2 * assign1
prelim = 0.5 * exam1 + 0.5 * cs1

# MIDTERM CALCULATION
cs2 = 0.5 * hoa2 + 0.3 * quiz2 + 0.2 * assign2
midterm = (1/3 * prelim) + (2/3 * (0.5 * exam2 + 0.5 * cs2))

# FINAL CALCULATION
cs3 = 0.5 * hoa3 + 0.3 * quiz3 + 0.2 * assign3
final = (1/3 * midterm) + (2/3 * (0.5 * exam3 + 0.5 * cs3))

# CONVERT TO UCC NUMERICAL GRADE
def convert_to_ucc_grade(grade):
    if grade >= 96:
        return 1.00
    elif grade >= 94:
        return 1.25
    elif grade >= 91:
        return 1.50
    elif grade >= 88:
        return 1.75
    elif grade >= 85:
        return 2.00
    elif grade >= 83:
        return 2.25
    elif grade >= 80:
        return 2.50
    elif grade >= 78:
        return 2.75
    elif grade >= 75:
        return 3.00
    else:
        return 5.00

ucc_grade = convert_to_ucc_grade(final)

# OUTPUT
print("\nFinal Results")
print(f"Student Name: {name}")
print(f"Prelim Grade: {prelim:.2f}")
print(f"Midterm Grade: {midterm:.2f}")
print(f"Final Grade: {final:.2f}")
print(f"UCC Numerical Grade: {ucc_grade:.2f}")
