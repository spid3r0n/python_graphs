nums = [1, 2, 3, 4, 5]
numbers = (1, 2, 3, 4, 5)
setofNumbers = {}

print(type(list))
print(type(numbers))
print(type(setofNumbers))
print("========================")


nums.reverse()
numbers = numbers[::-1]
print(nums) 
print(numbers)
print(setofNumbers)
print("=========================    ")

print(isinstance(nums, list))
print(isinstance(numbers, tuple))
print(isinstance(setofNumbers, dict))