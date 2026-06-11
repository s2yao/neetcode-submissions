class Solution:
    def isPalindrome(self, s: str) -> bool:
        # processing to make the symbols go away: isalum
        processed = []

        for i in range(len(s)):
            if s[i].isalnum():
                processed.append(s[i].lower())
        print(processed)

        return processed == processed[::-1]
