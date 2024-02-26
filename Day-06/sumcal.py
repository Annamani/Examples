# s=sum([10,20,30])
# print(s)
# s=[10,20,30,40]
# print(sum(s))

# Dict
def dict_sum(nums):
   num_sum = 0
   for i in nums:
       num_sum = num_sum + nums[i]
   return num_sum

nums = {'a': 100, 'b': 200, 'c': 300, 'd': 120}

print(type(nums))
print("Sum of all items of the said container:", dict_sum(nums))

# Set
nums = {7, 4, 9, 1, 3, 2}
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))


# Tuple
nums = (7, 4, 9, 1, 3, 2)
print("The original container")
print(nums)
print(type(nums))
sum_tuple = sum(nums)
print("Sum of all items of the said container:", str(sum_tuple))
