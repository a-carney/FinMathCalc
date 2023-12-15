import math
import errno
"""
Based on the study material for the actuarial FM exam. 

I would like to create a simple command line utility using python to calculate the following:
1. Time value of money
2. Annuities
3. Loans
4. Bonds
5. Yield rates
6. Duration
7. Immunization
8. Options
9. Swaps
10. Forwards and Futures
11. Interest rate derivatives
12. Financial analysis
"""


def solveForPV(i, PMT, FV, n):
    v = 1 / (1 + i)
    PV_OF_PMT = PMT * (1 - v**n) / i
    PV_OF_FV = FV * v**n
    return PV_OF_PMT + PV_OF_FV

def solveForFV(i, PMT, PV, n):
    FV_OF_PMT = PMT * ((1 + i)**n - 1) / i
    FV_OF_PV = PV * (1 + i)**n
    return FV_OF_PMT + FV_OF_PV

def solveForPMT(i, PV, FV, n):
    v = 1 / (1 + i)
    PMT_OF_PV = PV * i / (1 - v**n)
    PMT_OF_FV = FV * i / ((1 + i)**n - 1)
    return PMT_OF_PV + PMT_OF_FV

def solveForN(i, PV, PMT, FV):
    v = 1 / (1 + i)
    n = math.log((PMT - FV * i) / (PMT + PV * i)) / (2 * math.log(v))
    return n

def solveForI(PV, PMT, FV, n):
    for n in range(1, 10000):
        i = n / 10000
        if solveForPV(i, PMT, FV, n) - PV < 0.01:
            return i
        elif solveForFV(i, PMT, PV, n) - FV < 0.01:
            return i
        elif solveForPMT(i, PV, FV, n) - PMT < 0.01:
            return i
        elif solveForN(i, PV, PMT, FV) - n < 0.01:
            return i
        else:
            errno.EINVAL
        
        
            


def TVM():
    print("Enter value or ? for param")
    I = input("Interest rate: ")
    PV = input("Present value: ")
    PMT = input("Payment: ")
    FV = input("Future value: ")
    N = input("Number of periods: ")
    F =  input("Frequency (e.g. '2M' or '3Y') : ")

    if I == "?":
        I = solveForI(float(PV), float(PMT), float(FV), float(N))
        print("Interest rate: ", I)
    
    elif PV == "?":
        PV = solveForPV(float(I), float(PMT), float(FV), float(N))
        print("Present value: ", PV)
    
    elif PMT == "?":
        PMT = solveForPMT(float(I), float(PV), float(FV), float(N))
        print("Payment: ", PMT)

    elif FV == "?":
        FV = solveForFV(float(I), float(PMT), float(PV), float(N))
        print("Future value: ", FV)
    
    elif N == "?":
        N = solveForN(float(I), float(PV), float(PMT), float(FV))
        print("Number of periods: ", N)
    
    else:
        print("Invalid input")
