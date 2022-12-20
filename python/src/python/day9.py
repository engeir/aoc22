"""Day 9."""


from python import util


def tail_follow_head() -> None:
    lines = util.read_input("9")
    init_h: list[tuple[int, int]] = [(0, 0)]
    init_t: list[tuple[int, int]] = [(0, 0)]
    init_h_app = init_h.append
    init_t_app = init_t.append
    for line in lines:
        dir, steps = line.split()
        for _ in range(int(steps)):
            h, t = do_moves(dir, init_h[-1], init_t[-1])
            init_h_app(h)
            init_t_app(t)
    print(len(set(init_t)))  # 5907


def do_moves(
    dir: str, pos_h: tuple[int, int], pos_t: tuple[int, int]
) -> tuple[tuple[int, int], tuple[int, int]]:
    l_h, r_h = pos_h
    match dir:
        case "U":
            r_h -= 1
        case "R":
            l_h += 1
        case "L":
            l_h -= 1
        case "D":
            r_h += 1
    pos_t = catch_up((l_h, r_h), pos_t)
    return (l_h, r_h), pos_t


def catch_up(pos_h: tuple[int, int], pos_t: tuple[int, int]) -> tuple[int, int]:
    l_h, r_h = pos_h
    l_t, r_t = pos_t
    if abs(r_h - r_t) <= 1 and abs(l_h - l_t) <= 1:
        return l_t, r_t
    # move up/down
    if l_h == l_t:
        if r_h < r_t:
            r_t -= 1
        else:
            r_t += 1
    # move right/left
    elif r_h == r_t:
        if l_h < l_t:
            l_t -= 1
        else:
            l_t += 1
    # move diagonally
    else:
        r_t = r_t + 1 if r_t < r_h else r_t - 1
        l_t = l_t + 1 if l_t < l_h else l_t - 1
    return l_t, r_t


def ten_tail_follow_head() -> None:
    lines = util.read_input("9")
    init_h: list[tuple[int, int]] = [(0, 0)]
    init_1: list[tuple[int, int]] = [(0, 0)]
    init_2: list[tuple[int, int]] = [(0, 0)]
    init_3: list[tuple[int, int]] = [(0, 0)]
    init_4: list[tuple[int, int]] = [(0, 0)]
    init_5: list[tuple[int, int]] = [(0, 0)]
    init_6: list[tuple[int, int]] = [(0, 0)]
    init_7: list[tuple[int, int]] = [(0, 0)]
    init_8: list[tuple[int, int]] = [(0, 0)]
    init_t: list[tuple[int, int]] = [(0, 0)]
    init_h_app = init_h.append
    init_1_app = init_1.append
    init_2_app = init_2.append
    init_3_app = init_3.append
    init_4_app = init_4.append
    init_5_app = init_5.append
    init_6_app = init_6.append
    init_7_app = init_7.append
    init_8_app = init_8.append
    init_t_app = init_t.append
    for line in lines:
        dir, steps = line.split()
        for _ in range(int(steps)):
            h, t1 = do_moves(dir, init_h[-1], init_1[-1])
            init_h_app(h)
            init_1_app(t1)
            t2 = catch_up(init_1[-1], init_2[-1])
            init_2_app(t2)
            t3 = catch_up(init_2[-1], init_3[-1])
            init_3_app(t3)
            t4 = catch_up(init_3[-1], init_4[-1])
            init_4_app(t4)
            t5 = catch_up(init_4[-1], init_5[-1])
            init_5_app(t5)
            t6 = catch_up(init_5[-1], init_6[-1])
            init_6_app(t6)
            t7 = catch_up(init_6[-1], init_7[-1])
            init_7_app(t7)
            t8 = catch_up(init_7[-1], init_8[-1])
            init_8_app(t8)
            t = catch_up(init_8[-1], init_t[-1])
            init_t_app(t)
    print(len(set(init_t)))  # 2303


def part1() -> None:
    tail_follow_head()


def part2() -> None:
    ten_tail_follow_head()


if __name__ == "__main__":
    part1()
    part2()
