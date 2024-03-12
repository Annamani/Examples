# License: https://bit.ly/3oLErEI

# Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    return nums.count(19) == 2 and nums.count(5) >= 3

nums = [19, 19, 15, 5, 3, 5, 5, 2]
print(test(nums))
nums = [19, 19, 5, 5, 5, 5, 5]
print(test(nums))
