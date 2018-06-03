class Solution(object):
    def exit(self, board, word):
        """
        :type board: List[list[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0] or not word:
            return False
        m = len(board)
        n = len(board[0])
        self.m = m
        self.n = n
        self.board = board
        self. word = word
        visited = []
        for i in range(m):
            for j in range(n):
                if self.search(i, j, 0, visited):
                    return True
        return False
    def search(self, i, j, pos, visited):
        if not self.board[i][j] == self.word[pos]:
            return False
        if pos == len(self.word)-1:
            return True
        visited.append((i, j))
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            if i+di<0 or j+dj<0 or i+di>=self.m or j+dj>=self.n:
                continue
            elif (i,j) in visited:
                continue
            else:
                if self.search(i+di, j+dj, pos+1, visited):
                    return True
        visited.remove((i, j))
        return False
    def __init__(self):
        self.m = None
        self.n = None
        self.word = None
        self.board = None

