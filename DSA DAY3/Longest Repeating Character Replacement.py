#self brut forse pass some test cases
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s1 = list(s)
        left = 0
        max_len = 0
        tndx = len(s)
        temp = 'z'

        if k == 0:
            for right in range(len(s)):
                if s1[right] != s1[left]:
                    left= right 
                max_len = max(max_len, (right - left) + 1)

        else:
            for right in range(len(s)):

                if s1[right] != s1[left]:
                    # operation
                    if k > 0:

                        if right < tndx:
                            tndx = right
                            temp = s1[right]

                        s1[right] = s1[left]
                        k -= 1

                    else:
                        s1[tndx] = temp
                        left = tndx
                        right = left

                max_len = max(max_len, (right - left) + 1)

        return max_len
#optimize will pass all test cases
