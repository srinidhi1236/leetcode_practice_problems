class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        for i in range(n):
            direction = nums[i] > 0
            slow = fast = i

            while True:
                a = (slow + nums[slow]) % n
                b = (fast + nums[fast]) % n
                c = (b + nums[b]) % n

                if (nums[a] > 0) != direction:
                    break
                if (nums[b] > 0) != direction:
                    break
                if (nums[c] > 0) != direction:
                    break

                slow = a
                fast = c

                if slow == fast:
                    if slow == (slow + nums[slow]) % n:
                        break
                    return True

        return False
