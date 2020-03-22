"""
Triple step problem 8.1 CTCI
"""


class TripleStep:
    def __init__(self):
        self.memo = dict()
        self.memo[1] = 1
        self.memo[2] = 2
        self.memo[3] = 4

    def compute_steps(self, step):
        if self.memo.get(step):
            return self.memo[step]
        self.memo[step] = self.compute_steps(step-1) + self.compute_steps(step-2) + self.compute_steps(step-3)
        return self.memo[step]


if __name__ == "__main__":
    print(TripleStep().compute_steps(40))