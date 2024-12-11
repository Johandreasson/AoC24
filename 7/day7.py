with open(r'path/to/input', "r") as f:
    input = f.read().splitlines()


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
        print(equation)
        for i in range(3**(len(nums)-1)):
            test_sum = nums[0]
            trinary = []
            temp = i
            for _ in range(len(nums)-1): 
                trinary.append(temp % 3) 
                temp //= 3
            for j in range(len(nums)-1):
                if trinary[j] == 2:
                    test_sum = int(str(test_sum) + str(nums[j+1]))
                elif trinary[j] == 1:
                    test_sum *= nums[j+1]
                else:
                    test_sum += nums[j+1]
            if test_sum == this_sum:
                new_sum += this_sum
                break
    return new_sum

if __name__ == "__main__":
    invalid = []
    first_sum = part1()
    print(first_sum)
    print(part2(first_sum))