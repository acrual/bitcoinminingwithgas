

class Site(object):
    def __init__(self, hashrateVariation, btcPriceVariation, revenues=Revenues(), variablecost=Variablecost(), energysource=Energysource(), depreciations=Depreciations(), taxes=Taxes(), capex=Capex()):
        self.revenues = revenues
        self.variablecost = variablecost
        self.energysource = energysource
        self.depreciations = depreciations
        self.taxes = taxes
        self.capex = capex
        self.hashrateVariation = hashrateVariation
        self.btcPriceVariation = btcPriceVariation
        

    def __str__(self):
        return "This is the site"

    def btcRevenuesOfMonth(self, n):
        return revenues.monthlyrevenueBTCmonthOne * ((1 - self.hashrateVariation) ** n)

    def usdRevenuesOfMonth(self, n):
        return revenues.monthlyrevenueUSDmonthOne * ((1 - self.btcPriceVariation) ** n)

    def listOfBtcMonthlyRevenues(self):
        for i in range(60):
            list.append(self.btcRevenuesOfMonth(i))
        return list

    def listOfUsdMonthlyRevenues(self):
        for i in range(60):
            list.append(self.usdRevenuesOfMonth(i))
        return list


    
