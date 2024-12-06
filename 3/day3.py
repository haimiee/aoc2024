import sys
import re # Regex aka Regular Expressions

def part1(file_contents):
# Extracts pairs of numbers matching the pattern "mul(num1,num2)"
# using the regex `r"mul\(([0-9]+),([0-9]+)\)"`, then converts the 
# numbers to integers, multiplies each pair, and sums the results
    ans = sum([int(i) * int(j) for i, j in (re.findall(r"mul\(([0-9]+),([0-9]+)\)", file_contents))])

    print(f"Sum of the results of all the multiplications: {ans}")

def part2(file_contents):
    filtered_data = (re.findall(r"mul\(([0-9]+),([0-9]+)\)|(do\(\))|(don't\(\))", file_contents))
    flag = True
    ans = 0

    for tuple in filtered_data:
        for i, string in enumerate(tuple):
            if string == "don't()":
                flag = False
                break
            if string == "do()":
                flag = True
                break
            if not string:
                continue
            if string and flag:
                product = int(tuple[i]) * int(tuple[i + 1])
                ans += product
                break

    print(f"Sum of the results of the enabled multiplications: {ans}")


def main():
    # The contents of the test file will be into a string, for now it's empty
    file_contents = ""

    # When running the program in the console,
    # the second argument will be the opened file
    with open(sys.argv[1]) as f:
            file_contents = f.read() # The entire file is now the string for file_contents

    part1(file_contents)
    part2(file_contents)

main()