# 1.Write a function named sum_tothat accepts a single integer, n, and returns the sum of the integers from 1 to n.

def sum_to (n): 
    nums = list(range(n,0, -1))   # [6,5,4,3,2,1]
    sum = 0
    for idx in range(len(nums)):    # index of the num list above
        sum = sum + nums[idx]       # sum = 0 + num[0], equals 6                             
    return sum

print(sum_to(10))

# using method sum()

# def sum_to (num): 
#     nums = list(range(num,0, -1))
#     total = sum(nums)
#     return total


# 2. Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums): 
    largest= nums[0]
    print(nums)
    for num in nums: 
        if num > largest: 
            largest= num

    return largest

print(largest([1,2,3,4,0]))


def occurances (str, char): 
    count = 0
    if len(char) == 1: 
        for letter in str: 
            if letter == char:
                count  = count + 1
    if len(char) > 1: 
        count = str.count(char)

    return count
print("#3")   
print(occurances ('fleep floop', 'ee'))


# 4. Write a function named productthat takes an arbitrary number of numbers, multiplies them all together, and returns the product.


def product (*arg): 
    answer = 1
    for num in arg: 
        answer = answer * num
    return answer

print(product(-1, 4))