def main() -> None:
    """Print all three-digit numbers where sum of digits equals product."""
    for i in range(100, 1000):
        d1 = i // 100
        d2 = (i // 10) % 10
        d3 = i % 10

        s = d1 + d2 + d3
        p = d1 * d2 * d3

        if s == p:
            print(i)


if __name__ == "__main__":
    main()
