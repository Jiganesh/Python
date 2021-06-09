dictionary = {}
nums = [2,7,11,15]
target=9

for i in range (len(nums)):
    if target-nums[i] in dictionary:
        print(dictionary[target-nums[i]],i)
    else:
        dictionary[nums[i]]=i