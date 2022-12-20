def remove_duplicat(nums):
    first_pointer, second_pointer = 0, 0
    
    while second_pointer < len(nums):
        while second_pointer + 1 < len(nums) and nums[second_pointer] == nums[second_pointer+1]:
            second_pointer += 1
        nums[first_pointer] = nums[second_pointer]
        first_pointer += 1
        second_pointer += 1
    return print(nums[:first_pointer])

a = [0, 0, 0, 1, 2, 2, 3, 3, 3, 4]


remove_duplicat(a)