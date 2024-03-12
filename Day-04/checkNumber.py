# License: https://bit.ly/3oLErEI

# Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    # Check if the count of 19 in 'nums' is equal to 2 and the count of 5 is greater than or equal to 3
    return nums.count(19) == 2 and nums.count(5) >= 3

# Create a list 'nums' with specific elements
nums = [19, 19, 15, 5, 3, 5, 5, 2]
print(test(nums))
nums = [19, 19, 5, 5, 5, 5, 5]
print(test(nums))
