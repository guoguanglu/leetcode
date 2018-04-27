#count(up)==count(down)and count(right)==count(left)
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        strslist=list(moves)
        if strslist.count('U')==strslist.count('D') and strslist.count('L')==strslist.count('R'):
            return True
        else:
            return False