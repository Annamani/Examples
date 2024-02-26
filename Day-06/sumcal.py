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

# Set
# Create a set 'nums' with a collection of numbers.
nums = {7, 4, 9, 1, 3, 2}
# Print a message indicating the original container and display the set 'nums'.
print("The original container")
print(nums)
# Print the type of the 'nums' container.
print(type(nums))
# Calculate the sum of all items in the set 'nums' using the 'sum' function and store it in the 'sum_tuple' variable.
sum_tuple = sum(nums)
# Print the sum of all items in the set.
print("Sum of all items of the said container:", str(sum_tuple))
