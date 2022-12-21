"""Day 10."""


from python import util


def part1() -> None:
    lines = util.read_input("10")
    out = create_cycle_values(lines)
    strengths = sum(out[n] * n for n in [20, 60, 100, 140, 180, 220])
    print(strengths)  # 17020


def part2() -> None:
    lines = util.read_input("10")
    out = create_cycle_values(lines)
    drawn = draw_cycles(out)
    print(drawn)
    # RLEZFLGE
    # ###  #    #### #### #### #     ##  #### 
    # #  # #    #       # #    #    #  # #    
    # #  # #    ###    #  ###  #    #    ###  
    # ###  #    #     #   #    #    # ## #    
    # # #  #    #    #    #    #    #  # #    
    # #  # #### #### #### #    ####  ### #### 


def create_cycle_values(cycle_steps: list[str]) -> dict[int, int]:
    """Create the value at each cycle.

    Parameters
    ----------
    cycle_steps: list[str]
        The cycle instructions.

    Returns
    -------
    list[tuple[int, int]]
        A list of tuples, with cycle number and the current value.
    """
    values = {}
    x = 1
    cycle = 0
    for value in cycle_steps:
        if value.startswith("noop"):
            cycle += 1
            values[cycle] = x
        elif value.startswith("addx"):
            cycle += 1
            values[cycle] = x
            cycle += 1
            values[cycle] = x
            x += int(value.split()[-1])
    values[-1] = x
    return values


def draw_cycles(cycle_values: dict[int, int]) -> str:
    drawing = ""
    for i, v in cycle_values.items():
        n = i - 1
        if not n % 40:
            drawing += "\n"
        n = n % 40
        drawing += "#" if n in [v, v - 1, v + 1] else " "
    return drawing


if __name__ == "__main__":
    part1()
    part2()
