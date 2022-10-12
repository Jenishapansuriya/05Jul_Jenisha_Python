nums = []
n=int(input("Enter the number of list elements:"))
for i in range(n):
  nums.append(int(input()))

small = nums[0]
for i in range(n):
  if small>nums[i]:
    small = nums[i]

secondSmall = nums[0]
for i in range(n):
  if secondSmall>nums[i]:
    if nums[i]!=small:
      secondSmall=nums[i]

print("\nSecond Smallest Number is: ")
print(secondSmall)