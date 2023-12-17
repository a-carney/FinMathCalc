import math
import errno

class TVM:
    def __init__(self, i=None, PV=None, PMT=None, FV=None, n=None):
        self.i = i
        self.PV = PV
        self.PMT = PMT
        self.FV = FV
        self.n = n

    def solve_for_pv(self):
        v = 1 / (1 + self.i)
        pv_of_pmt = self.PMT * (1 - v**self.n) / self.i
        pv_of_fv = self.FV * v**self.n
        return pv_of_pmt + pv_of_fv

    def solve_for_fv(self):
        fv_of_pmt = self.PMT * ((1 + self.i)**self.n - 1) / self.i
        fv_of_pv = self.PV * (1 + self.i)**self.n
        return fv_of_pmt + fv_of_pv

    def solve_for_pmt(self):
        v = 1 / (1 + self.i)
        pmt_of_pv = self.PV * self.i / (1 - v**self.n)
        pmt_of_fv = self.FV * self.i / ((1 + self.i)**self.n - 1)
        return pmt_of_pv + pmt_of_fv

    def solve_for_n(self):
        v = 1 / (1 + self.i)
        n = math.log((self.PMT - self.FV * self.i) / (self.PMT + self.PV * self.i)) / (2 * math.log(v))
        return n

    def solve_for_i(self):
        for n in range(1, 10000):
            i = n / 10000
            self.i = i
            if self.solve_for_pv() - self.PV < 0.01:
                return i
            elif self.solve_for_fv() - self.FV < 0.01:
                return i
            elif self.solve_for_pmt() - self.PMT < 0.01:
                return i
            elif self.solve_for_n() - self.n < 0.01:
                return i
            else:
                errno.EINVAL
    
def tvm_calculator():
    print("Enter value or ? for param")
    i = float(input("Interest rate: ") or 0)
    PV = float(input("Present value: ") or 0)
    PMT = float(input("Payment: ") or 0)
    FV = float(input("Future value: ") or 0)
    n = float(input("Number of periods: ") or 0)

    calculator = TVM(i=i, PV=PV, PMT=PMT, FV=FV, n=n)

    if '?' in [i, PV, PMT, FV, n]:
        if i == '?':
            print("Interest rate: ", calculator.solve_for_i())
        elif PV == '?':
            print("Present value: ", calculator.solve_for_pv())
        elif PMT == '?':
            print("Payment: ", calculator.solve_for_pmt())
        elif FV == '?':
            print("Future value: ", calculator.solve_for_fv())
        elif n == '?':
            print("Number of periods: ", calculator.solve_for_n())
    else:
        print("Invalid input")

