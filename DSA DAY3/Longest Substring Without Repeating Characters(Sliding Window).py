class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

self approch
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Mx=0
        Cnt=0
        start=0
        myD=set()
        i=0
        while i < len(s):
            # add in dictionary and increase freq
            if s[i] in myD:
                start+=1
                i=start
                myD.clear()
                Mx=max(Cnt,Mx)
                myD.add(s[i])
                Cnt=1
                i+=1
            else:
                myD.add(s[i])
                Cnt+=1
                Mx=max(Cnt,Mx)
                i+=1

        return Mx



