# s=sum([10,20,30])
# print(s)
# s=[10,20,30,40]
# print(sum(s))
# Define a function 'dict_sum' that takes a dictionary 'nums' as input and calculates the sum of its values.
def dict_sum(nums):
   num_sum = 0
   for i in nums:
       num_sum = num_sum + nums[i]
   return num_sum

nums = {'a': 100, 'b': 200, 'c': 300, 'd': 120}

print(type(nums))
print("Sum of all items of the said container:", dict_sum(nums))

