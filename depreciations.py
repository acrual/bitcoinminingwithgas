class Depreciations(object):
    def __init__(self, minerExpectedLife, gensetExpectedLife):
        self.minerExpectedLife = minerExpectedLife
        self.gensetExpectedLife = gensetExpectedLife

    def __str__(self):
        return "This site will have this depreciation"