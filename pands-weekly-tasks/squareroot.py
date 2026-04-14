# squareroot.py
## This program takes a positive floating=point number as input and outputs an aproximation of its square root.
## Author: Leah Curran

def sqrt(S, tolerance=1e-12, max_iter=100):
    """
    Approximate sqrt(S) using Newton's (Babylonian/Heron's) method.

    Parameters:
        S (float): positive number to square-root (S >= 0)
        tolerance (float): how accurate we want the answer
        max_iter (int): safety cap to avoid infinite loops

    Returns:
        float: approximation of sqrt(S)
    """
    if S < 0:
        raise ValueError("sqrt() only supports non-negative numbers (real square roots).")
    if S == 0:
        return 0.0

    # A simple initial guess:
    # - If S >= 1, start at S (easy and works)
    # - If 0 < S < 1, start at 1 so we don't start *too* small
    guess = S if S >= 1.0 else 1.0

    for _ in range(max_iter):
        # Newton/Babylonian update: next = (guess + S/guess) / 2
        next_guess = 0.5 * (guess + S / guess)

        # Stop if we've converged (difference is very small)
        if abs(next_guess - guess) <= tolerance * max(1.0, abs(next_guess)):
            return next_guess

        guess = next_guess

    # If we hit max_iter, return the best we have (or raise an error—your choice)
    return guess


def main():
    S = float(input("Enter a positive number: "))
    print("Approximate square root:", sqrt(S))


if __name__ == "__main__":
    main()