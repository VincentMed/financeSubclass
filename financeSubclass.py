# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:38:26 2021
@author: 16617
Interest rate problem
given 2 o 3, solve for the last one
"""

class loan(object):
    def __init__(self, name):
        self._name = name
        
    def who(self):
        print(self._name)
        
    def setPV(self, PV):
        self._PV = PV
        print('Amount borrowed = ', self._PV)
        
    def setRate(self, ratePct):
        #set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')
        
    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')
        return self._months
        
    def computePmt(self):
        # formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)
        r = self._ratePct/100/12
        self._Pmt = self._PV*(r*(1+r)**self._months)/((1+r)**self._months-1)
        print('Monthly payment = $', round(self._Pmt,2))
        return self._Pmt

class creditCards(loan):
    def __init__(self, name):
        loan.__init__(self, name)
        
    def getBalance(self):
        self.balance = self._months * self._Pmt
        print(f"Current Balance is ${self.balance:.2f}")     

if __name__ == "__main__":
    # loan1 = loan('Dr J')
    # loan1.who()

    # loan1.setPV(27150)  #mini cooper
    # loan1.setRate(1.9)
    # loan1.setMonths(42)
    # payment = loan1.computePmt()

    creditCard1 = creditCards(input("Enter name of Credit Card"))
    creditCard1.who()
    creditCard1.setPV(1000)
    creditCard1.setRate(12)
    creditCard1.setMonths(12)
    payment = creditCard1.computePmt()
    creditCard1.getBalance()

    creditCard2 = creditCards(input("Enter name of Credit Card"))
    creditCard2.who()
    creditCard2.setPV(5000)
    creditCard2.setRate(10)
    creditCard2.setMonths(12)
    payment = creditCard2.computePmt()
    creditCard2.getBalance()
