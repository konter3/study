def remove_duplicat(nums):
    first_pointer, second_pointer = 0, 0
    
    while second_pointer < len(nums):
        while second_pointer + 1 < len(nums) and nums[second_pointer] == nums[second_pointer+1]:
            second_pointer += 1
        nums[first_pointer] = nums[second_pointer]
        first_pointer += 1
        second_pointer += 1
    return print(nums[:first_pointer])



def nums_append_to_list(nums):
    for i in range(len(nums)):
        b.append(int(nums[i]))
    return b
        
nums = input()
b = []

nums_append_to_list(nums)
remove_duplicat(sorted(b))