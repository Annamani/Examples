# Enter a list with positive and negative numbers
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ", nums)
# new_nums = list(filter(lambda x: x > 0, nums))
new_nums=[num for num in nums if num >= 0]
print("Positive numbers in the said list: ", new_nums)
