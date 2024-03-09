# License: https://bit.ly/3oLErEI

# Define a function named 'test' that takes a list 'nums' as input
def test(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3

# Create a list 'nums' with specific elements
nums = [19, 19, 15, 5, 5, 5, 1, 2]
print("Original list:")
print(nums)
print(test(nums))

# Create a different list 'nums' with specific elements
nums = [19, 15, 5, 7, 5, 5, 2]
print("\nOriginal list:")
print(nums)
print(test(nums))

# Create another list 'nums' with specific elements
nums = [11, 12, 14, 13, 14, 13, 15, 14]
print("\nOriginal list:")
print(nums)
print(test(nums))

# Create one more list 'nums' with specific elements
nums = [19, 15, 11, 7, 5, 6, 2]
print("\nOriginal list:")
print(nums)
print(test(nums))
