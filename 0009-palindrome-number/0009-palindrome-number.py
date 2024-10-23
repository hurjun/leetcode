class Solution(object):
    def isPalindrome(self, x):
        temp = list(str(x))
        reversed_x = temp[::-1]
        y="".join(reversed_x)
        x=str(x)
        if y==x:
            return True
        else:
            return False

        