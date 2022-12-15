"""Day 6."""


from python import util


def detect_unique_segment(code: str, length: int) -> int:
    for j, _ in enumerate(code[length - 1 :]):
        candidate = code[j : j + length]
        if len(set(candidate)) == length:
            return j + length
    raise ValueError(f"Could not find any markers in {code}.")


def part1() -> None:
    lines = util.read_input("6")[0]
    marker_index = detect_unique_segment(lines, 4)
    print(marker_index)  # 1282


def part2() -> None:
    lines = util.read_input("6")[0]
    marker_index = detect_unique_segment(lines, 14)
    print(marker_index)  # 3513


if __name__ == "__main__":
    part1()
    part2()
