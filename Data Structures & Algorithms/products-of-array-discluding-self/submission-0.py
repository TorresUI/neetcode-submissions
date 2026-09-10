class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        postfix = deque([nums[-1]])
        res = []
        for n in range(1, len(nums)):
            prefix.append(nums[n] * prefix[-1])

        for i in range(len(nums) - 2, -1, -1):
            postfix.appendleft(nums[i] * postfix[0])

        for n in range(len(nums)):
            if n == 0:
                res.append(postfix[n + 1])
            elif n == len(nums) - 1:
                res.append(prefix[n - 1])
            else:
                res.append(prefix[n - 1] * postfix[n + 1])
        return res
