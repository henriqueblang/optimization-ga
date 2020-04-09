class BitSet:
    def __init__(self, size):
        self.bits = (1 << size) - 1

    def get(self, index):
        return (self.bits >> index) & 1

    def set(self, index, value):
        mask = 1 << index

        self.bits &= ~mask

        if value:
            self.bits |= mask

    def flip(self, index):
        self.bits ^= (1 << index)
