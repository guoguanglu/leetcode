#two points, one: cur_point ,two : newchars_point
#then from left to right, get the same character count,
#if count>1, character and count give newchars point position
#or only character give newchars point positon
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cur_point=0
        newchars_point=0
        count=0
        temp = chars[0]
        length = len(chars)
        while cur_point <length:
            if temp!= chars[cur_point]:
                chars[newchars_point]=temp
                newchars_point +=1
                if count>1:
                    chars[newchars_point:newchars_point+len(str(count))]=list(str(count))
                    newchars_point += len(str(count))
                temp = chars[cur_point]
                count=0
            else:
                count+=1
                cur_point+=1
        chars[newchars_point]=temp
        newchars_point +=1
        if count>1:
            chars[newchars_point:newchars_point+len(str(count))]=list(str(count))
            newchars_point += len(str(count))
        return newchars_point