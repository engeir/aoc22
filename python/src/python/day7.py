"""Day 7."""


from python import util


def create_tree_from_stdin_stdout(lines: list[str]) -> dict:
    tree: dict[str, dict | str] = {"/": {}}
    level = ["/"]
    for line in lines[1:]:
        if line.startswith("dir"):  # Only creates new, deeper and deeper
            tree = make_new_directory(tree, level, line[4:])
        elif line.startswith("$ cd .."):
            level.pop()
        elif line.startswith("$ cd"):
            level.append(line[5:])
        elif line[0].isnumeric():
            tree = make_new_file(tree, level, line)
    return tree


def make_new_directory(tree: dict, level: list, newdir: str) -> dict:
    level_copy = level.copy()
    level_copy.append(newdir)
    tmp = tree[level_copy[0]]
    try:
        for i, _ in enumerate(level_copy[1:]):
            full_depth = "|".join(level_copy[: i + 2])
            if i == len(level_copy[1:]) - 1:
                tmp[full_depth] = {}
                tmp = tmp[full_depth]
                return tree
            tmp = tmp[full_depth]
    except Exception as e:
        raise KeyError(
            f"Tried with {level_copy[-1] = }, {tmp = }, {level_copy = }"
        ) from e
    return tree


def make_new_file(tree: dict, level: list, file: str) -> dict:
    tmp = tree[level[0]]
    for i, _ in enumerate(level[1:]):
        full_depth = "|".join(level[: i + 2])
        tmp = tmp[full_depth]
        if i == len(level[1:]) - 1:
            tmp[file.split()[1]] = file.split()[0]
            return tree
    return tree


def cd(tree: dict, path: list[str]) -> dict:
    cwd = tree
    for p in path:
        cwd = cwd[p]
    return cwd


def sum_func(indict: dict, acc, path=None) -> int:
    if path is None:
        path = ["/"]
    nowdict = cd(indict, path)
    ls = nowdict.keys()
    size = sum(
        sum_func(indict, acc, path + [name])
        if isinstance(nowdict[name], dict)
        else int(nowdict[name])
        for name in ls
    )
    acc.append(size)
    return size


def part1(sl: list[int]) -> None:
    # Find all of the directories with a total size of at most 100000
    print(sum(s for s in sl if s < 100_000))  # 1084134


def part2(sl: list[int]) -> None:
    # Total disk space is 70_000_000, and the update need at least 30_000_000.
    # Find the smallest directory that would make the available space more than
    # 30_000_000.
    print(min(s for s in sl if sl[0] - s < 40_000_000))  # 6183184


if __name__ == "__main__":
    lines = util.read_input("7")
    tree = create_tree_from_stdin_stdout(lines)
    sizes: list[int] = []
    sum_func(tree, sizes)
    sizes.reverse()
    part1(sizes)
    part2(sizes)
