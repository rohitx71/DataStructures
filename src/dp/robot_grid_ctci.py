class RobotGrid:
    def __init__(self):
        self.rows, self.cols = 5,5
        self.memo = [[0]*self.rows]*self.cols
        self.memo[4][4] = 1
        self.memo[0][2] = -1
    def find_goal(self, i, j):
        if self.memo[i][j] != 0:
            return self.memo[i][j]
        if self.memo[i][j] == -1:
            return -1
        if self.memo[i][j] == 1:
            return 1 + self.memo[i][j]
        if i == self.rows:
            if self.find_goal(i+1,j) == 1:
                self.memo[i + 1][j] = 1
                return 1
            else:
                self.memo[i+1][j] = -1
        if j != self.cols:
            if self.find_goal(i, j+1) == 1:
                self.memo[i][j+1] = 1
                return 1
            else:
                self.memo[i][j+1] = -1
        return -1


if __name__ == "__main__":
    r = RobotGrid()
    print(r.find_goal(0,0))
    print(r.memo)