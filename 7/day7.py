import math

with open(r'C:\Users\JANDRE21\Repos\AoC24\7\input.txt', "r") as f:
    input = f.read().splitlines()

test="""190: 10 19
        3267: 81 40 27
        83: 17 5
        156: 15 6
        7290: 6 8 6 15
        161011: 16 10 13
        192: 17 8 14
        21037: 9 7 18 13
        292: 11 6 16 20"""


def part1():
    valid_sum = 0
    for equation in input:
        this_sum = int(equation.split(": ")[0])
        nums = [int(num) for num in equation.split(": ")[1].split()]
        valid = False
        for i in range(2**(len(nums)-1)):
            test_sum = nums[0]
            for j in range(len(nums)-1):
                if i & (1<<(len(nums)-2-j)):
                    test_sum *= nums[j+1]
                else:
                    test_sum += nums[j+1]
            if test_sum == this_sum:
                valid_sum += this_sum
                valid = True
                break
        if not valid:
            invalid.append(equation.lstrip())
    return valid_sum

def part2(new_sum):
    for equation in invalid:
        this_sum = int(equation.split(": ")[0])
        nums = [int(num) for num in equation.split(": ")[1].split()]

        for i in range(3**(len(nums)-1)):
            test_sum = nums[0]
            trinary = []
            temp = i
            for _ in range(len(nums)-1):  # Convert the number to 4 trinary digits
                trinary.append(temp % 3)  # Get the remainder (trinary digit)
                temp //= 3  # Update the number for the next digit
            print(trinary)
            print("".join(map(str, reversed(trinary))))  # Print digits in reverse order
    return new_sum

if __name__ == "__main__":
    input = test.splitlines()
    invalid = []
    first_sum = part1()
    print(first_sum)
    print(part2(first_sum))