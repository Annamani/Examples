# from functools import reduce
# nums = [10, 20, 30]
# print("Original list numbers:")
# print(nums)
# nums_product = reduce((lambda x, y: x * y), nums)
# print("\nProduct of the said numbers (without using a for loop):", nums_product)

import math
nums = [10, 20, 30]
nums_product = math.prod(nums)
print("\nProduct of the said numbers (without using a for loop):", nums_product)

