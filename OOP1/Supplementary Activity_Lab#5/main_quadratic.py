from quadratic_solver import solve_quadratic

def write_to_file(a, b, c, roots):
    """
    Writes the inputs and outputs to a text file.
    """
    with open("quadratic_results.txt", "a") as file:
        file.write(f"Inputs: a = {a}, b = {b}, c = {c}\n")
        file.write("Roots:\n")
        for root in roots:
            file.write(f"  {root}\n")
        file.write("\n")

def get_user_input():
    """
    Prompts the user to input coefficients a, b, and c.
    """
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    return a, b, c

def main():
    """
    Main function to solve the quadratic equation and write results.
    """
    a, b, c = get_user_input()
    roots = solve_quadratic(a, b, c)
    write_to_file(a, b, c, roots)
    print("Roots:")
    for root in roots:
        print(root)

if __name__ == "__main__":
    main()