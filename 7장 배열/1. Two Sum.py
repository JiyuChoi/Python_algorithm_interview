# 브루트포스로 계산
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색
def twoSum(nums, target):
    for i, n in enumerate(nums):
        if target - n in nums[i+1:]:
            return [i, nums[i+1:].index(target-n)+(i+1)]


# 첫번째 수를 뺀 결과 키 조회
def twoSum(nums, target):
    nums_map = {}
    for i, n in enumerate(nums):
        nums_map[n] = i

    for i, n in enumerate(nums):
        if target - n in nums_map and i != nums_map[target-n]:
            return [i, nums_map[target-n]]

print(twoSum([2, 7, 11, 15], 9))