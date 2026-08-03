class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict(int)
        ret = 0
        left = 0
        for right in range(len(s)):
            if s[right] not in visited:
                visited[s[right]] = right
            else: # shinking
                if visited[s[right]] >= left:
                    left = visited[s[right]] + 1
                visited[s[right]] = right
            ret = max(ret, right - left + 1)
        
        return ret

# ret = 3
# abcabcbb
# l = 0 r = 2
# dict a0 b1 c2 