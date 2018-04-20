#the core code is that stop condition is sqrt(num)
#because,one factor can get two factors numbers
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return False
        list = []
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                if i != num / i:
                    list.append(num / i)
                list.append(i)

        if sum(list) - num == num:
            return True
        else:
            return False