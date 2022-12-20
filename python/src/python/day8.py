"""Day 8."""


import numpy as np

from python import util


def string2array() -> np.ndarray:
    lines = util.read_input("8")
    np_lines = np.zeros((len(lines), len(lines[0])))
    for i, line in enumerate(lines):
        np_lines[:, i] = np.array([int(j) for j in line])
    return np_lines


def find_visible_trees(trees: np.ndarray) -> int:
    count = trees.shape[0] * 2 + (trees.shape[1] - 2) * 2
    for i in range(1, trees.shape[0] - 1):
        for j in range(1, trees.shape[1] - 1):
            if trees[i, j] > max(trees[:i, j]):
                count += 1
            elif trees[i, j] > max(trees[i + 1 :, j]):
                count += 1
            elif trees[i, j] > max(trees[i, j + 1 :]):
                count += 1
            elif trees[i, j] > max(trees[i, :j]):
                count += 1
    return count


def most_scenic_location(trees: np.ndarray) -> int:
    view = 0
    for i in range(1, trees.shape[0] - 1):
        for j in range(1, trees.shape[1] - 1):
            this_view = 1
            this_view *= consecutive_smaller_than(trees[i, j], trees[:i, j][::-1])
            this_view *= consecutive_smaller_than(trees[i, j], trees[i + 1 :, j])
            this_view *= consecutive_smaller_than(trees[i, j], trees[i, j + 1 :])
            this_view *= consecutive_smaller_than(trees[i, j], trees[i, :j][::-1])
            view = max(this_view, view)
    return view


def consecutive_smaller_than(tree: int, trees: np.ndarray) -> int:
    count = 0
    for num in trees:
        count += 1
        if num >= tree:
            break
    return count


def part1() -> None:
    trees = string2array()
    count = find_visible_trees(trees)
    print(count)  # 1533


def part2() -> None:
    trees = string2array()
    view = most_scenic_location(trees)
    print(view)  # 345744


if __name__ == "__main__":
    part1()
    part2()
