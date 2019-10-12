class Miners(object):
    def __init__(self, brand, model, hashesseg, consumption, price, extracosts):
        self.brand = brand
        self.model = model
        self.hashesseg = hashesseg
        self.consumption = consumption
        self.price = price
        self.extracosts = extracosts
        self.consumptionRatio = self.consumption / self.hashesseg
        self.powercostratio = (self.price * self.extracosts) / self.consumption
        self.hashratecostratio = (self.price * self.extracosts) / self.hashesseg
        


    def __str__(self):
        return "these are this miner's characteristics"

    