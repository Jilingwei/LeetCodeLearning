# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
class two_sum:
    def twoSum(nums, target):
        lens = len(nums)
        j = -1
        for i in range(0, lens):
            temp = nums[(i+1):]
            if (target - nums[i]) in temp:
                j = temp.index(target - nums[i])
                break
        if j >= 0:
            return [j, i]
