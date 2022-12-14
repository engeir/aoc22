"""Global functions used across many scripts."""


def read_input(day: str) -> list[str]:
    with open(f"./../input/day{day}.txt", "r") as f:
        lines = f.readlines()
    return [line.strip("\n") for line in lines]
