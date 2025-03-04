#region imports
from math import sqrt, pi, exp
from NumericalMethods import GPDF, Simpson, Probability
#endregion
from NumericalMethods import GaussSeidel

#region function definitions

def main():
    # Define the augmented matrix [A | b]
    Aaug = [
        [3, 1, -1, 2],
        [2, 4, 1, 12],
        [-1, 2, 5, 10]
    ]

    # Initial guess vector
    x = [0, 0, 0]

    # Number of iterations
    Niter = 20

    # Call the GaussSeidel function
    solution = GaussSeidel(Aaug, x, Niter)

    # Print the solution
    print("Solution vector (x):", solution)

def main():
    """
    I want to integrate the Gaussian probability density function between
    a left hand limit = (mean - 5*stDev) to a right hand limit = (c).  Here
    is my step-by-step plan:
    1. Decide mean, stDev, and c and if I want P(x>c) or P(x<c).
    2. Define args tuple and c to be passed to Probability
    3. Pass args, and a callback function (GPDF) to Probability
    4. In probability, pass along GPDF to Simpson along with the appropriate args tuple
    5. Return the required probability from Probability and print to screen.
    :return: Nothing to return, just print results to screen.
    """

    #region testing user input
    # The following code solicites user input through the CLI.
    mean = input("Population mean? ")
    stDev = input("Standard deviation?")
    c = input("c value?")
    GT = True if input("Probability greater than c?").lower() in ["y","yes","true"] else "False"
    print("P(x"+(">" if GT else "<") + c +"|"+mean+", "+stDev +")")
    #endregion
#endregion

if __name__ == "__main__":
    main()
