import math

class ARBIT:
    def __init__(self, seed):
        self.N = seed
        self.value = 0
        self.A = 16807
        self.Q = 127773
        self.R = 2836
        self.C = 2147483647
        
    def next(self):
        X = self.A * (self.N%self.Q) - self.R * (self.N//self.Q)
        if X < 0:
            self.N = X + self.C
        else:
            self.N = X
        return self.N / self.C

    def sample(self, n):
        result = []
        for _i in range(n):
            result.append(self.next())
        return result

class RNG:
    def __init__(self, seed):
        self.seed = seed
        self.ARBIT = ARBIT(seed)
        self.room = self.ARBIT.sample(32)

    def update_seed(self, seed):
        self.seed = seed
        self.ARBIT = ARBIT(seed)
        self.room = self.ARBIT.sample(32)

    def next(self):
        x = self.ARBIT.next()
        y = math.trunc(32 * self.ARBIT.next())
        temp = self.room[y]
        self.room[y] = x
        return temp

    def reset(self):
        self.ARBIT = ARBIT(self.seed)
        self.room = self.ARBIT.sample(32)

    def sample(self, n):
        result = []
        for _i in range(n):
            result.append(self.next())
        return result

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def myran(n=1, seed=1):
    if myran.calls == 1:
        myran.rn = RNG(seed)
    else:
        pass

    if seed != 1:
        myran.rn.update_seed(seed)
        return
    if n == 1:
        return myran.rn.next()
    elif n == -1:
        myran.rn.reset()
    else:
        return myran.rn.sample(n)

