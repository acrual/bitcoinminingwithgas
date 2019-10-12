

class Variablecost(object):
    def __init__(self, poolcost, powersupplycost, oandm):
        self.poolcost = poolcost # percentage
        self.powersupplycost = powersupplycost # vendrá de energysource y este dependerá de si es de gas o no
        self.oandm = oandm

    def __str__(self):
        return "this is the variablecost"

    