class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for char in s:
            # if character is a valid character
            if char.isalnum():
                new_str += char.lower()
        print(new_str)
        return new_str == new_str[::-1]