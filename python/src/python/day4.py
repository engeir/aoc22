"Day 4."


from python import util


def two_regions_to_one(regions: str) -> tuple[str, str, str]:
    """A pair of regions are combined to one."""
    # One region is on the format
    # int-int
    # That is, two integers separated by a hyphen. The regions are separated by a comma.
    r1, r2 = regions.split(",")
    b1, t1 = r1.split("-")
    b2, t2 = r2.split("-")
    b3 = b1 if int(b1) < int(b2) else b2
    t3 = t1 if int(t1) > int(t2) else t2
    return r1, r2, f"{b3}-{t3}"


def full_overlap(regions: tuple[str, str, str]) -> bool:
    """Check if one region fully covers the other."""
    return regions[0] == regions[2] or regions[1] == regions[2]


def partial_overlap(regions: tuple[str, str, str]) -> int:
    """Check if the two regions overlap at all."""
    b1, t1 = regions[0].split("-")
    b2, t2 = regions[1].split("-")
    b3, t3 = regions[2].split("-")
    return (
        0
        if (b1 == b3 and t2 == t3 and int(t1) < int(b2))
        or (b2 == b3 and t1 == t3 and int(t2) < int(b1))
        else 1
    )


def part1() -> None:
    """Part 1 of day 4."""
    day4 = util.read_input("4")
    summ = 0
    for pair in day4:
        region_tuples = two_regions_to_one(pair)
        out = full_overlap(region_tuples)
        o = 1 if out else 0
        summ += o
    print(summ)  # 450


def part2() -> None:
    """Part 2 of day 4."""
    day4 = util.read_input("4")
    summ = 0
    for pair in day4:
        region_tuples = two_regions_to_one(pair)
        out = partial_overlap(region_tuples)
        summ += out
    print(summ)  # 837


if __name__ == "__main__":
    part1()
    part2()
