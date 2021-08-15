class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if len([int(i) for i in str(num)]) == 1:
                return sum([int(i) for i in str(num)])
            else:
                num = sum([int(i) for i in str(num)])
                
