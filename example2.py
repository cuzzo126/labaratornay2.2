import math
import sys


def main():
    """Вычисление квадратного корня с проверкой a >= 0."""
    a = float(input("Value of a? "))
    if a < 0:
        print("Illegal value of a!", file=sys.stderr)
        sys.exit(1)
    
    x, eps = 1, 1e-10
    while True:
        xp = x
        x = (x + a / x) / 2
        if math.fabs(x - xp) < eps:
            break
    print(f"x = {x:.10f}")


if __name__ == "__main__":
    main()
