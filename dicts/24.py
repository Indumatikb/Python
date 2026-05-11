class Solution:
    def longest(self, s):
        max_len = 0

        for i in range(len(s)):
            seen = ""
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen = seen + s[j]

            if len(seen) > max_len:
                max_len = len(seen)

        return max_len


obj = Solution()
print(obj.longest("abcabcbb"))