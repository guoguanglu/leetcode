# method
#1: remove symbol
#2: get word
#3: compute count
#4: get the most common
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in "!?',;.":
            paragraph=paragraph.replace(i,'')
        paragraph=paragraph.lower()
        listword=paragraph.split()
        ret =''
        for elem in listword:
            if elem not in banned:
                if listword.count(elem)>listword.count(ret):
                    ret=elem
        return ret