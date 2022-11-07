# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:07:39 2022

@author: Vincent Medrano

add a class to example class
class creditCards(finance):
sub class of finance, contains at least 2 credit cards : name, balance
and monthly payment.
function to get total owed
function to get monthly total payments to CCs
"""

class loan(object):
    def __init__(self, name):
        self._name= name
        
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
        print('payment = $', round(self._Pmt,2))
        return self._Pmt
    
class creditCards(object):
    def __init__(self, cc_name, cc_balance):
        self.cc_name = cc_name
        self.cc_balance = 2000
        cc_balance = self.cc_balance - cc_balance
        
        print(f"Credit card {cc_name} has a balance of ${cc_balance}.")

class finance(creditCards):
    def get_total(cc_balance):
        return cc_balance

        
    
        

if __name__ == "__main__":
    loan1 = loan('Dr J')
    loan1.who()

    loan1.setPV(27150)  #mini cooper
    loan1.setRate(1.9)
    loan1.setMonths(42)
    payment = loan1.computePmt()
    
    credit1 = creditCards("Amex", 600)
    credit2 = creditCards("Visa", 1300 )