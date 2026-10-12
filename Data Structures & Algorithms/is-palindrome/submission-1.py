
class Solution:
    def isAlphaNumeric(self, char: str) -> bool:
        ascii_value = ord(char)

        if (
            48 <= ascii_value <= 57
            or 97 <= ascii_value <= 122
            or 65 <= ascii_value <= 90
        ):
            return True

        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isAlphaNumeric(s[left]):
                left += 1
                continue

            if not self.isAlphaNumeric(s[right]):
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True