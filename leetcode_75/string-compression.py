# 443. String Compression
# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        if not chars:
            return None
        
        read =  0
        start = 0
        end = 0
        write  = 0

        while read < len(chars):
            curr = chars[read]
            end = start = read
            chars[write] = chars[start]
            write += 1
            while read < len(chars) and chars[read] == curr:
                end = read
                read += 1

            if end - start == 0:
                continue

            count = str(end - start + 1)

            for ch in count:
                chars[write] = ch
                write += 1


        return write
            
        

sol = Solution()
# nums = ["a", "b", "c"]
# nums = ["a","a","b","b","c","c","c"]
# nums = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
nums = ["a","a","a","b","b","a","a"]
len = sol.compress(nums)
print(len, nums[:len])