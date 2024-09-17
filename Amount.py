# Psuedocode from Module 5.2
# https://canvas.oregonstate.edu/courses/1967322/pages/exploration-5-dot-2-backtracking-combination-sum-problem?module_item_id=24505907

from copy import deepcopy

def combination_sum_helper(nums, start, result, remainder, combination):
    if remainder == 0: # no reminder meaning everything from combination list are the numbers that add up to the target
        result.append(deepcopy(combination))
        return
    if remainder < 0: # sum is too high
        return 

    for i in range(start, len(nums)):
        # ensure we do not try to find duplicate sets/lists
        # since the list is sorted we can compare the previous start to the current and see if we have already checked for this number or not. 
        if i > start and nums[i] == nums[i - 1]: 
            continue
        combination.append(nums[i])

        # i + 1 ensures we do not use numbers twice unlike the pseudocode provided.
        # with i, we will see a longer result list especially if the initial list has the number 1 in it. 
        combination_sum_helper(nums, i + 1, result, remainder - nums[i], combination) 

        combination.pop()

def amount(A, S):
    result = []
    A.sort()
    # print(A)
    # print(S)
    combination_sum_helper(A, 0, result, S, [])
    return result



def main():

    A1 = [11,1,3,2,6,1,5]
    S1 = 8
    result = amount(A1,S1)
    print(result)
    # print(amount([2,3,6,7], 7 ))
    # print(amount([11,1,3,2,6,1,5], 8))
    # print(amount([2,4,2,6,2,8], 6))


main()