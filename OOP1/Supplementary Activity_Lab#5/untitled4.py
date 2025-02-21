from quadratic_solver import solve_quadratic

def write_to_file(a, b, c, roots):
    with open("quadratic_results.txt", "a") as file:
        file.write(f"Inputs: a = {a}, b = {b}, c = {c}\n")
        file.write("Roots:\n")
        for root in roots:
            file.write(f"  {root}\n")
        file.write("\n")  
def main():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    roots = solve_quadratic(a, b, c)
    write_to_file(a, b, c, roots)

    print("Roots:")
    for root in roots:
        print(root)

if __name__ == "__main__":
    main()