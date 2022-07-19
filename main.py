# ДЗ 6. Протоколи, наслідування, поліморфізм

from colors import bcolors
class frange:
    def __init__(self, A, L=None, D=None):
        self.A = A
        self.L = L
        self.D = D



    def __next__(self):

        if self.L == None:
            self.L = self.A + 0.0
            self.A = 0.0
        if self.D == None:
            self.D = 1.0

        if self.D > 0 and self.A >= self.L:
            raise StopIteration("Limit exceeded")
        elif self.D < 0 and self.A <= self.L:
            raise StopIteration("Limit exceeded")


        result = self.A
        self.A = self.D + result

        return result

    def __iter__(self):

        return self


assert (list(frange(5)) == [0, 1, 2, 3, 4])
assert (list(frange(2, 5)) == [2, 3, 4])
assert (list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert (list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert (list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert (list(frange(1, 5)) == [1, 2, 3, 4])
assert (list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert (list(frange(0, 0)) == [])
assert (list(frange(100, 0)) == [])

print('SUCCESS!')

class colorizer:
    def __init__(self, color='red'):
        self.color = getattr(bcolors, color)


    def __enter__(self):
        self.text = print(f"{self.color}")
        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{bcolors.ENDC}")

with colorizer(color="green"):
    print('printed in green')
print('printed in default color')





