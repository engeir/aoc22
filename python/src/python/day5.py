"Day 5."


from python import util


def split_crate_stack_from_instructions() -> tuple[list[str], list[str]]:
    lines = util.read_input("5")
    crates = []
    instructions = []
    for i, ell in enumerate(lines):
        if i < 9:
            crates.append(ell)
        elif i == 9:
            continue
        else:
            instructions.append(ell)
    return crates, instructions


def create_crate_lists(crates: list[str]) -> list[list[str]]:
    # Each column is three characters wide, and they are spaced with one white space.
    # However, the only important information is kept at the middle character in each
    # column. Meaning, column number 2, 2+4, 2+4+4, etc.
    # The last row thus gives us their number and index.
    rev = crates[:-1]
    rev.reverse()
    table = crates[-1]
    crate_numbers = table.split()
    crate_idxs = [table.find(i) for i in crate_numbers]
    ordered_crates: list[list[str]] = [[] for _ in range(int(crate_numbers[-1]))]
    for line in rev:
        for idx, num in zip(crate_idxs, crate_numbers):
            if line[idx].isalpha():
                ordered_crates[int(num) - 1].append(line[idx])
    return ordered_crates


def crate_mover_9000(
    ordered_crates: list[list[str]], moves: list[str]
) -> list[list[str]]:
    for move in moves:
        out = move.split()
        amount, off, on = int(out[1]), int(out[3]), int(out[5])
        for _ in range(amount):
            remove = ordered_crates[off - 1].pop()
            ordered_crates[on - 1].append(remove)
    return ordered_crates


def crate_mover_9001(
    ordered_crates: list[list[str]], moves: list[str]
) -> list[list[str]]:
    for move in moves:
        out = move.split()
        amount, off, on = int(out[1]), int(out[3]), int(out[5])
        for a in range(amount):
            remove = ordered_crates[off - 1].pop(a - amount)
            ordered_crates[on - 1].append(remove)
    return ordered_crates


def read_top(crates: list[list[str]]) -> str:
    return "".join(column[-1] for column in crates)


def part1() -> None:
    c, i = split_crate_stack_from_instructions()
    order = create_crate_lists(c)
    updated = crate_mover_9000(order, i)
    top = read_top(updated)
    print(top)  # FRDSQRRCD


def part2() -> None:
    c, i = split_crate_stack_from_instructions()
    order = create_crate_lists(c)
    updated = crate_mover_9001(order, i)
    top = read_top(updated)
    print(top)  # HRFTQVWNN


if __name__ == "__main__":
    part1()
    part2()
