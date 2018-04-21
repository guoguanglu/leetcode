#use stack ,if elem =="})]",then stack[-1]must"{(["
#then pop stack[-1],or stack.append[elem]
#finally ,if stack is empty, True,or False
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[1]
        for i in s:
            if i ==')':
                if stack[-1]=='(':
                    stack.pop(len(stack)-1)
                    continue
            elif i==']':
                if stack[-1]=='[':
                    stack.pop(len(stack)-1)
                    continue
            elif i=='}':
                if stack[-1]=='{':
                    stack.pop(len(stack)-1)
                    continue
            stack.append(i)
        if len(stack)==1:
            return True
        else:
            return False