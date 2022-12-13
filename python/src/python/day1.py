"""Day 1."""


def _read() -> list[str]:
    with open("./../input/day1.txt", "r") as f:
        lines = f.readlines()
    return [line.strip("\n") for line in lines]


def count_segments(all_calories) -> list[int]:
    """Count up until a blank element, then start over."""
    individual_cals = []
    sum_cal = 0
    for cal in all_calories:
        if cal == "":
            individual_cals.append(sum_cal)
            sum_cal = 0
        else:
            sum_cal += int(cal)
    individual_cals.append(sum_cal)
    individual_cals.sort()
    return individual_cals


def find_highest_individual(sorted_list: list[int]) -> int:
    """Return the last value."""
    return sorted_list[-1]


def find_sum_of_top_three(sorted_list: list[int]) -> int:
    """Return the sum of the three last last values."""
    return sum(sorted_list[-3:])


if __name__ == "__main__":
    sorted_list = count_segments(_read())
    most_calories = find_highest_individual(sorted_list)
    print(most_calories)  # 71124
    top_three_calories = find_sum_of_top_three(sorted_list)
    print(top_three_calories)  # 204639
