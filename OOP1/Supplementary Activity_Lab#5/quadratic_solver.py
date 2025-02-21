import math

def solve_quadratic(a, b, c):
    """
    Solves the quadratic equation ax^2 + bx + c = 0.
    Returns a tuple of roots (real or complex).
    """
    discriminant = b**2 - 4*a*c

    if discriminant > 0: 
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:  
        root = -b / (2*a)
        return (root,)
    else:  
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (
            complex(real_part, imaginary_part),
            complex(real_part, -imaginary_part)
        )