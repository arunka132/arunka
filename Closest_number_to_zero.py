documentation: str = """
Leet Code problem: 2239. Find Closest Number to Zero
Problem discription:

Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
If there are multiple answers, return the number with the largest value.

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
"""
import pdb

class Solution:
    def __init__(self):
        pass
    def closest_num(self, arr: list[int]) -> int:
        """
        :approch: use abs() for non negative elements
        :Time:
        :Space:
        :param arr: list of elements
        :return: int closest number to zero
        """
        closest = arr[0]
        for i in range(len(arr)):
            if abs(arr[i]) < abs(closest):
                closest = arr[i]
        for i in range(len(arr)):
            closest = abs(closest) if closest < 0 and abs(closest) in arr else closest
        return closest

if __name__ == "__main__":
    # pdb.set_trace()
    sol = Solution()
    _1 = [-4,-2,1,4,8]
    _2 = [2,-1,1]
    merge = [_1, _2]
    for i in merge:
        rst = sol.closest_num(i)
        print(rst)

