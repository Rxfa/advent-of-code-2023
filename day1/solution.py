import time
def main():
    """Main function"""
    with open("input.txt") as f:
        lines = f.readlines()
        acc = 0
        for line in lines:
            acc += get_numbers(line.strip())
    return acc
            
def get_numbers(line):
    """Gets first and last digit out of a line of strings"""
    left = 0
    right = len(line) - 1
    while (left < right) and not (line[left].isdigit() and line[right].isdigit()):
        if not line[left].isdigit():
            left += 1
        if not line[right].isdigit():
            right -= 1
    return int(line[left] + line[right])

if __name__ == "__main__":
    main()
