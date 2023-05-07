class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        answer1, answer2 = [], []

        nums1_map = {}

        for num1 in nums1:

            nums1_map[num1] = 1

        for num2 in nums2:

            if nums1_map.get(num2, -1) == -1:

                answer2.append(num2)
                nums1_map[num2] = 2

            else:

                nums1_map[num2] = 0

        for num1 in nums1:

            if nums1_map[num1] == 1:

                answer1.append(num1)
                nums1_map[num1] = 0

        answer = []

        answer.append(answer1)
        answer.append(answer2)

        return answer
