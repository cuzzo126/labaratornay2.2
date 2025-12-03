def get_japanese_year_name(year: int) -> str:
    """Return Japanese calendar name (color + animal) for given year.
    Base year: 1984 = green mouse.
    """
    animals = [
        "mouse", "cow", "tiger", "rabbit", "dragon", "snake",
        "horse", "sheep", "monkey", "rooster", "dog", "pig",
    ]
    colors = ["green", "red", "yellow", "white", "black"]

    offset = year - 1984

    # 12-year animal cycle
    animal_index = offset % 12
    animal = animals[animal_index]

    # 10-year color cycle, each color lasts 2 years
    color_index = (offset % 10) // 2
    color = colors[color_index]

    return f"{color} {animal}"


def main() -> None:
    """Read year and print its Japanese calendar name."""
    year = int(input("Enter year: "))
    name = get_japanese_year_name(year)
    print(f"{year} is the year of the {name}.")


if __name__ == "__main__":
    main()
