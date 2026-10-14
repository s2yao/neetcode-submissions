class Solution:
    def longestPalindrome(self, s: str) -> str:
        def detect(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return [max(0, l + 1), min(len(s), r - 1)]
        curr_left = 0
        curr_right = 0

        for i in range(len(s)):
            odd_left, odd_right = detect(i, i)
            even_left, even_right = detect(i, i+1)
            # print(odd_left, odd_right)
            # print(even_left, even_right)

            odd_len = odd_right - odd_left + 1
            even_len = even_right - even_left + 1

            if curr_right - curr_left + 1 < even_len:
                curr_left, curr_right = even_left, even_right
            if curr_right - curr_left + 1 < odd_len:
                curr_left, curr_right = odd_left, odd_right
        print(curr_left, curr_right, "end")
        return s[curr_left:curr_right+1]