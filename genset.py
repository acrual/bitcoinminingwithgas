class Genset(object):
    def __init__(self, name, power, price, btuhour, efficiency, maintenance):
        self.name = name
        self.power = power
        self.price = price
        self.btuhour = btuhour
        self.efficiency = efficiency
        self.maintenance = maintenance

    def __str__(self):
        return "el motor de gas es así: "