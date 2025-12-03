import math
import sys

EULER = 0.5772156649015328606
EPS = 1e-10


def main():
    """Вычисление exp(x) через ряд Тейлора."""
    x = float(input("Value of x? "))
    if x == 0:
        print("Illegal value of x!", file=sys.stderr)
        sys.exit(1)
    
    a = x
    S, k = a, 1
    while math.fabs(a) > EPS:
        k += 1
        a = x ** k / math.factorial(k)
        S += a
    
    print(f"e^x = {math.exp(x):.10f}")
    print(f"EULER + ln|x| = {EULER + math.log(math.fabs(x)):.10f}")
    print(f"S = {S:.10f}")


if __name__ == "__main__":
    main()
