class MinerPortfolio(object):
    def __init__(self, numMiners, qtyList=[], minerList=[]):
        self.qtyList = qtyList
        self.minerList = minerList

    def __str__(self):
        return "El portfolio de mineros está compuesto por X tipos con y, z, a, b cada uno"