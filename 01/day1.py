import sys
from typing import List
import heapq
from collections import Counter

def read_lines(filename: str) -> List[str]:
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve1(filename: str) -> int:
    lines = read_lines(filename)

    firsts, seconds = [], []
    for line in lines:
        first, second = line.split()
        heapq.heappush(firsts, int(first))
        heapq.heappush(seconds, int(second))

    result = 0
    while firsts:
        result += abs(heapq.heappop(firsts) - heapq.heappop(seconds))

    return result

def solve2(filename: str) -> int:
    lines = read_lines(filename)

    firsts, seconds = [], []
    result = 0
    for line in lines:
        first, second = line.split()
        firsts.append(int(first))
        seconds.append(int(second))

    counts = Counter(seconds)
    return sum([first * counts[first] for first in firsts])

print("Day 1:")
print(f"  Part 1: {solve1(sys.argv[1])}")
print(f"  Part 2: {solve2(sys.argv[1])}")
