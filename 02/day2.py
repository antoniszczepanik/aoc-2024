import sys
from typing import List
import heapq
from collections import Counter

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def is_safe(nums):
    diffs = [x-y for x,y in zip(nums, nums[1:])]
    directions = [d > 0 for d in diffs]
    in_range = [abs(d) > 0 and abs(d) < 4 for d in diffs]
    return (all(directions) or not any(directions)) and all(in_range)

def solve1(filename: str) -> int:
    lines = read_lines(filename)
    result = 0
    for line in lines:
        nums = [int(n) for n in line.split()]
        if is_safe(nums):
            result += 1
    return result

def solve2(filename: str) -> int:
    lines = read_lines(filename)
    result = 0
    for line in lines:
        nums = [int(n) for n in line.split()]
        for skip in range(len(nums)):
            if is_safe(nums[0:skip] + nums[skip+1:]):
                result += 1
                break
    return result

print("Day 1:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
