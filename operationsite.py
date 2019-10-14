from revenues import Revenues
from variablecost import *
from energysource import *
from depreciations import *
from taxes import *
from capex import *


class Site(object):
    def __init__(self, hashrateVariation, btcPriceVariation, revenues, variablecost, energysource, depreciations, taxes, capex):
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
        return self.revenues.monthlyrevenueBTCmonthOne() * ((1 - self.hashrateVariation) ** n)

    def usdRevenuesOfMonth(self, n):
        return self.revenues.monthlyrevenueUSDmonthOne() * ((1 - self.btcPriceVariation) ** n)

    def listOfBtcMonthlyRevenues(self):
        for i in range(60):
            list.append(self.btcRevenuesOfMonth(i))
        return list

    def listOfUsdMonthlyRevenues(self):
        for i in range(60):
            list.append(self.usdRevenuesOfMonth(i))
        return list


    
