from savings import *

class Revenues(object):
    def __init__(self, minersPerContainer, miningYield, mmdd, savings):
        self.minersPerContainer = minersPerContainer
        self.miningYield = miningYield
        self.mmdd = mmdd
        self.savings = savings
        # hacer script para extraer precio de bitcoin de la base de datos y meter el dato en self.bitcoinPrice
        self.bitcoinPrice = 5

    def __str__(self):
        return "These are the revenues for this site on date: " +str(self.mmdd)

    def monthlyrevenueBTCmonthOne(self):
        if self.numContainers > 0:
            return self.numContainers * self.minersPerContainer * self.miningYield 
        else:
            return self.minersPerContainer * self.miningYield

    def monthlyrevenueUSDmonthOne(self):
        if self.numContainers > 0:
            return self.numContainers * self.minersPerContainer * self.miningYield * self.bitcoinPrice
        else:
            return self.minersPerContainer * self.miningYield * self.bitcoinPrice







    