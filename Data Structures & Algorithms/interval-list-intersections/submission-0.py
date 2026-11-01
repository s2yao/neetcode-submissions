
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort()
        secondList.sort()

        curr_first_int = 0
        curr_second_int = 0
        ret = []

        while curr_first_int < len(firstList) and curr_second_int < len(secondList):
            start1 = firstList[curr_first_int][0]
            end1 = firstList[curr_first_int][1]
            start2 = secondList[curr_second_int][0]
            end2 = secondList[curr_second_int][1]
            
            
            if start1 <= end2 and start2 <= end1:
                ret.append([max(start1, start2), min(end1, end2)])

            if end1 < end2:
                curr_first_int += 1
            else:
                curr_second_int += 1
            
        
        return ret