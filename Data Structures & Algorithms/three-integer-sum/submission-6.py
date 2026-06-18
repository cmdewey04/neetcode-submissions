class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #[-4,-1,-1,0,1,2]
        results = []
        nums.sort()

       
        for nDx,num in enumerate(nums):
            if nDx > 0:
                if num == nums[nDx-1]:
                    continue

            l,r = nDx+1, len(nums)-1
            while l<r:
                total = nums[l] + nums[r] + num
                if total == 0:
                    newList = [nums[l], num, nums[r]]
                    results.append(newList)
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    l+=1
                    r-=1

                elif total > 0:
                    r-=1
                else:
                    l+=1
        return results

