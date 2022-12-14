"""Day 2."""

from python import util


def rules1(x: str, y: str) -> int:
    """Calculate score from a single game."""
    # Their
    # |  Mine
    # |  |
    # A, X = Rock (1)
    # B, Y = Paper (2)
    # C, Z = Scissors (3)
    # Lose = 0
    # Draw = 3
    # Win = 6
    match x, y:
        case "A", "X":
            return 3 + 1
        case "A", "Y":
            return 6 + 2
        case "A", "Z":
            return 0 + 3
        case "B", "X":
            return 0 + 1
        case "B", "Y":
            return 3 + 2
        case "B", "Z":
            return 6 + 3
        case "C", "X":
            return 6 + 1
        case "C", "Y":
            return 0 + 2
        case "C", "Z":
            return 3 + 3
        case _:
            raise ValueError(f"What is {x = } and {y = }?")


def rules2(x: str, y: str) -> int:
    """Calculate score from a single game."""
    # Their
    # |  Mine
    # |  |
    # A, X = Rock (1), Lose
    # B, Y = Paper (2), Draw
    # C, Z = Scissors (3), Win
    # Lose = 0
    # Draw = 3
    # Win = 6
    match x, y:
        case "A", "X":
            return 0 + 3
        case "A", "Y":
            return 3 + 1
        case "A", "Z":
            return 6 + 2
        case "B", "X":
            return 0 + 1
        case "B", "Y":
            return 3 + 2
        case "B", "Z":
            return 6 + 3
        case "C", "X":
            return 0 + 2
        case "C", "Y":
            return 3 + 3
        case "C", "Z":
            return 6 + 1
        case _:
            raise ValueError(f"What is {x = } and {y = }?")


def sum_games1() -> None:
    game_list = util.read_input("2")
    summ = sum(rules1(g[0], g[-1]) for g in game_list)
    print(summ)  # 11767


def sum_games2() -> None:
    game_list = util.read_input("2")
    summ = sum(rules2(g[0], g[-1]) for g in game_list)
    print(summ)  # 13886


if __name__ == "__main__":
    sum_games1()
    sum_games2()
