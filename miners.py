class Miners(object):
    def __init__(self, brand, model, hashesseg, consumption, price):
        self.brand = brand
        self.model = model
        self.hashesseg = hashesseg
        self.consumption = consumption
        self.price = price

    def __str__(self):
        return "these are this miner's characteristics"