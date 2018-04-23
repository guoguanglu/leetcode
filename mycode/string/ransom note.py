#method one , magazine remove elems of ransomNote
#method two , if ransomNote.count(elem)>magazine.count(elem),return False
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #method one
        '''        
        temp = list(magazine)
        for elem in ransomNote:
            if elem in temp:
                temp.remove(elem)
            else:
                return False
        return True'''
        #method two 
        for i in ransomNote:
            if ransomNote.count(i)>magazine.count(i):
                return False
        return True