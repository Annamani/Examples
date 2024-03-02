from functools import reduce
nums = [10, 20, 30]
print("Original list numbers:")
print(nums)
nums_product = reduce((lambda x, y: x * y), nums)

# Print the product of the numbers, obtained without using a for loop.
print("\nProduct of the said numbers (without using a for loop):", nums_product)
