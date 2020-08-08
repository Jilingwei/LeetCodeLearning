class test:
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

    if __name__ == "__main__":
        res = twoSum([3, 3], 6)
        print(res)
