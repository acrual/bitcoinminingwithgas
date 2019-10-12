class Capex(object):
    def __init__(self, numberOfContainers, minersCost=Miners(), replacementCost, setupCost):
        self.numberOfContainers = numberOfContainers
        self.minersCost = minersCost
        self.replacementCost = replacementCost
        self.setupCost = setupCost

    def __str__(self):
        return "Whatever"

    def