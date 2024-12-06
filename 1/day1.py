import sys 
from collections import defaultdict


def part1(file_contents):
    list1 = []
    list2 = []

    rows = file_contents.split("\n")

    # print(rows)

    for row in rows:
        two_nums = row.split("   ")
        # print(two_nums)
        list1.append(int(two_nums[0]))
        list2.append(int(two_nums[1]))

    list1.sort()
    list2.sort()
    
    ans = 0

    for i in range(len(list1)):
        distance = abs(list1[i] - list2[i])
        ans += distance
        
    print(f"Total Distance = {ans}")

def part2(file_contents):
    list1 = []
    freq = defaultdict(int)

    rows = file_contents.split("\n")

    for row in rows:
        two_nums = [int(i) for i in row.split("   ")] # Make list, then go over every item
        # print(two_nums)                             # in row and make each string into int
        list1.append(two_nums[0])
        freq[two_nums[1]] += 1

    # print(freq)
    
    similarity_score = 0

    for num in list1:
        if num in freq: # Dictionaries are magic, so checking if a num in it, ezpz
            similarity_score += freq[num] * num

    print(f"Similarity Score = {similarity_score}")


def main():
    file_contents = ""

    with open(sys.argv[1]) as f:
            file_contents = f.read()
    
    # print(file_contents)

    part1(file_contents)
    part2(file_contents)


main()