class SmallestInfiniteSet:

    def __init__(self):

        self.list = [n for n in range(1, 1000+1)]
        self.min = 1
        self.total = 1000

    def popSmallest(self) -> int:

        self.total -= 1

        for i in range(self.min-1, 1000+1):

            if self.list[i] != 0:

                self.list[i] = 0
                self.min = i+1
                return i+1
        
    def addBack(self, num: int) -> None:
        
        if self.list[num-1] == 0:
            
            self.list[num-1] = num
            self.total += 1
            self.min = min(self.min, num)
