class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = 1
        while x >= 10 * y:
            y *= 10

        while x:
            if x // y != x % 10:
                return False
            x = (x % y) // 10
            y = y / 100
        return True