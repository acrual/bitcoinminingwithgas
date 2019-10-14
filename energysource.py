from genset import *

class Energysource(object):
    def __init__(self, gasYesNo, gascost, electricityCost, genset):
        self.gasYesNo = gasYesNo
        if self.gasYesNo:
            self.genset = genset
            self.gascost = gascost
            self.electricityCost = 0
        else:
            self.electricityCost = electricityCost

    def __str__(self):
        return "This is the gensetmaintenance"


        
    

    
