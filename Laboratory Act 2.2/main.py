print("Enter all grades out of 100")

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

# OUTPUT
print("\nFinal Results")
print(f"Prelim Grade: {prelim:.2f}")
print(f"Midterm Grade: {midterm:.2f}")
print(f"Final Grade: {final:.2f}")
