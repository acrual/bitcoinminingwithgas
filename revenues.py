

class Revenues(object):
    def __init__(self, numContainers, minersPerContainer, miningYield, bitcoinProduction, bitcoinPrice, date, savings):
        self.numContainers = numContainers
        self.minersPerContainer = minersPerContainer
        self.miningYield = miningYield
        self.bitcoinProduction = bitcoinProduction
        self.bitcoinPrice = bitcoinPrice
        self.date = date
        self.savings = savings

    def __str__(self):
        return "These are the revenues for this site on date: " +str(self.date)

    