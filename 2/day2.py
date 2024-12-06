import sys 
from collections import defaultdict


def part1(file_contents): # Function to count how many safe reports

    # Make a list of items of each newline occurance (row)
    rows = file_contents.split("\n") 
    
    # Initialize 0 to the answer of the problem (number of safe reports)
    ans = 0
    
    # For every item in the list 'rows'
    for row in rows:
        asc = 0 # Initialize 0 for acending count
        desc = 0 # Initialize 0 for the descending count
        
        # Initialize every row to be a report
        report = [int(i) for i in row.split(" ")] # Modify into list where every item will
                                                  # be split by each " ", then turned to int
        
        for i in range(len(report) - 1):
            if not (1 <= abs(report[i] - report[i + 1]) <= 3):
                break
            if report[i] > report[i + 1]: # If number at this index is > the next,
                asc += 1                  # increment ascending count by 1
            if report[i] < report[i + 1]: # If number at this index is < the next,
                desc += 1                 # increment descending count by 1
        
        # If ascending or descending count reaches safe limit, increment safe reports count
        if asc == (len(report) - 1) or desc == (len(report) - 1):
            ans += 1
    
    print(f"{ans} reports are safe.")

def part2(file_contents): # Function to count how many safe reports using the 'Problem Dampener'
    rows = file_contents.split("\n")
    ans = 0

    for row in rows:
        report = [int(i) for i in row.split(" ")]
        
        for index_ignored in range(len(report)):
            asc = 0
            desc = 0
            temp_report = report[:index_ignored] + report[index_ignored + 1:]

            for i in range(len(temp_report) - 1):
                if not (1 <= abs(temp_report[i] - temp_report[i + 1]) <= 3):
                    break
                if temp_report[i] < temp_report[i + 1]:
                    asc += 1
                elif temp_report[i] > temp_report[i + 1]:
                    desc += 1

            if asc == len(temp_report) - 1 or desc == len(temp_report) - 1:
                ans += 1
                break
    
    print(f"Thanks to the Problem Dampener, {ans} reports are actually safe!")



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