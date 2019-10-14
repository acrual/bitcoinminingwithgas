from miners import *

class Capex(object):
    def __init__(self, numberOfContainers, minersCost, replacementCost, setupCost):
        self.numberOfContainers = numberOfContainers
        self.minersCost = minersCost
        self.replacementCost = replacementCost
        self.setupCost = setupCost

    def __str__(self):
        return "Whatever"
