class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        def is_Valid(c):
            valid = True
            if(ord(c.lower())>=97 and ord(c.lower())<=122):
                pass

            elif(ord(c.lower())>=48 and ord(c.lower())<=57):
                pass

            else:
                valid = False

            return valid
        
        while (left<=right):
            if(is_Valid(s[left])==False):
                left += 1
                continue
            
            if(is_Valid(s[right])==False):
                right -= 1
                continue
            
            if(s[left].lower() != s[right].lower()):
                return False

            else:
                left += 1
                right -= 1

        return True
