# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:07:39 2022
@author: Vincent Medrano
"""

class loan(object):
    def __init__(self, name):
        self._name = name
        
    def who(self):
        print(self._name)
        
    def setPV(self, PV):
        self._PV = PV
        print('present value = ', self._PV)
        
    def setRate(self, ratePct):
        #set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')
        
    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')
        
    def computePmt(self):
        # formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)
        r = self._ratePct/100/12
        self._Pmt = self._PV*(r*(1+r)**self._months)/((1+r)**self._months-1)
        print('Monthly payment = $', round(self._Pmt,2))
        return self._Pmt

    def makePayment(self, amount):
        self.amount = amount
        return self.amount

    def getBalance(self):
        self.total = self._Pmt * self._months - self.amount
        print(f"Thank you for your payment of ${self.amount}")
        print(f"New Balance = ${self.total:.2f}")

# add a class to example class
# class creditCards(loan):
# sub class of finance, contains at least 2 credit cards : name, balance
# and monthly payment.
# function to get total owed
# function to get monthly total payments to CCs    
class creditCards(loan):
    def __init__(self, name):
        super().__init__(name)        

if __name__ == "__main__":
    loan1 = loan('Dr J')
    loan1.who()

    loan1.setPV(27150)  #mini cooper
    loan1.setRate(1.9)
    loan1.setMonths(42)
    payment = loan1.computePmt()

    credit1 = creditCards("Amex")
    credit1.who()
    credit1.setPV(1000)
    credit1.setRate(10.0)
    credit1.setMonths(12)
    payment = credit1.computePmt()

    credit1.makePayment(500)
    credit1.getBalance()

    credit1 = creditCards("Discover")
    credit1.who()
    credit1.setPV(2000)
    credit1.setRate(18)
    credit1.setMonths(12)
    payment = credit1.computePmt()

    credit1.makePayment(500)
    credit1.getBalance()
