class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        fuck = defaultdict(int)
        fuck[0] = 1
        pref = 0

        for num in nums:
            pref += num
            modulo = pref % k
            ret += fuck[modulo]
            fuck[modulo] += 1
        
        return ret