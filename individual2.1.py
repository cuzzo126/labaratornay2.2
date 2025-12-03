def get_year_word(n: int) -> str:
    """Return the correct English word for years."""
    if n % 10 == 1 and n % 100 != 11:
        return "year"
    return "years"


def main() -> None:
    """Read n and print the phrase."""
    n = int(input("Enter an integer n (> 100): "))
    word = get_year_word(n)
    print(f"I am {n} {word} old")


if __name__ == "__main__":
    main()
