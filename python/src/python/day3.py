"""Day 3."""

from python import util


def find_common_character(chars: str) -> str:
    """Split string in two and find the common one in the two halves."""
    if len(chars) % 2:
        raise AttributeError(f"Something is wrong... {chars = }")
    p1 = chars[: len(chars) // 2]
    p2 = chars[len(chars) // 2 :]
    for p in p1:
        if p in p2:
            return p
    raise LookupError("Found nothing mate.")


def find_badges(char_list: tuple[str, str, str]) -> str:
    """Find the common character across the three strings in the tuple."""
    for c in char_list[0]:
        if c in char_list[1] and c in char_list[2]:
            return c
    raise LookupError("Found no common character..?")


def lookup_table(c: str) -> int:
    """Lookup table to give priority to characters."""
    alph = "abcdefghijklmnopqrstovwxyz"
    return (
        (alph.index(c.lower()) + 1) + 26 if c.isupper() else alph.index(c.lower()) + 1
    )


def part1() -> None:
    """Part 1 of day 3."""
    chars = util.read_input("3")
    summ = 0
    for c in chars:
        common = find_common_character(c)
        priority = lookup_table(common)
        summ += priority
    print(summ)  # 8202


def part2() -> None:
    """Part 2 of day 3."""
    chars = util.read_input("3")
    summ = 0
    it = iter(chars)
    for c1, c2, c3 in zip(it, it, it):
        badge = find_badges((c1, c2, c3))
        priority = lookup_table(badge)
        summ += priority
    print(summ)  # 2864


if __name__ == "__main__":
    part1()
    part2()
