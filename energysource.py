

class Energysource(object):
    def __init__(self, gasYesNo, gascost, electricityCost, genset=Genset()):
        self.gasYesNo = gasYesNo
        if self.gasYesNo:
            self.genset = genset
            self.gascost = gascost
        else:
            self.electricityCost = electricityCost

    def __str__(self):
        return "This is the gensetmaintenance"


        
    

    
