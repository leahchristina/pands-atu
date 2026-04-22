# squareroot.py
## This program takes a positive floating-point number as input and outputs an approximation of its square root.
## Author: Leah Curran

# Setting a tolerance to stop the guess when it's "close enough" and a max interation to prevent an infinite loop.
def sqrt(S, tolerance=1e-12, max_iter=100):
    """
    Approximate sqrt(S) using Newton's (Babylonian/Heron's) method. [1] (Improving a guess until it becomes very close to the true answer. When applied to square roots it becomes the Babylonian/Heron's method.)

    Parameters:
        S (float): positive number to square-root (S >= 0)
        tolerance (float): how accurate we want the answer
        max_iter (int): safety cap to avoid infinite loops

    Returns:
        float: approximation of sqrt(S) 
        Largely referencing code found online with some added error proofing. [2]
    """
    # Throw an error for a negative number, if S = 0 then the answer is immediately 0.
    if S < 0:
        raise ValueError
    if S == 0:
        return 0.0

    # Applying an initial guess:
    # - If S >= 1, start at S 
    # - If 0 < S < 1, start at 1 (so it's not too small)
    guess = S if S >= 1.0 else 1.0

    for _ in range(max_iter):
        # Newton/Babylonian update: next = (guess + S/guess) / 2
        next_guess = 0.5 * (guess + S / guess)

        # Stop if tolerance is hit
        if abs(next_guess - guess) <= tolerance * max(1.0, abs(next_guess)):
            return next_guess

        guess = next_guess

    # If we hit max_iter, return the best we have
    return guess


def main():
    S = float(input("Enter a positive number: "))
    print("Approximate square root:", sqrt(S))


if __name__ == "__main__":
    main()

# [1] https://www.andreaminini.net/math/iterative-method-for-calculating-square-roots
# [2] https://www.geeksforgeeks.org/dsa/find-root-of-a-number-using-newtons-method/