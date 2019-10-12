

class Site(object):
    def __init__(self, revenues=Revenues(), variablecost=Variablecost(), energysource=Energysource(), depreciations=Depreciations(), taxes=Taxes(), capex=Capex(), hashrateVariation, btcPriceVariation):
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


    def contributionMargin(self):


    
