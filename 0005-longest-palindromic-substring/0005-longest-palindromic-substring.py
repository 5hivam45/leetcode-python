class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        max_length = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left + 1, right - left - 1

        for i in range(len(s)):
            left1, length1 = expand(i, i)
            left2, length2 = expand(i, i + 1)

            if length1 > max_length:
                start = left1
                max_length = length1

            if length2 > max_length:
                start = left2
                max_length = length2

        return s[start:start + max_length]