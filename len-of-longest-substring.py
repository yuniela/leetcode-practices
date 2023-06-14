class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        setS = {}
        l = 0
        output = 0

        for character in range(len(s)):
            if s[character] not in setS:
                output = max(output, character-l+1)
            
            else:
                if setS[s[character]] < l:
                    output = max(output, character-l+1)

                else:
                    l = setS[s[character]] + 1
            setS[s[character]] = character

        return output

