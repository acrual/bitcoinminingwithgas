class Savings(object):
    def __init__(self, metric, limit, penaltybelow, penaltyabove):
        self.metric = metric
        self.limit = limit
        self.penaltybelow = penaltybelow
        self.penaltyabove = penaltyabove

    def __str__(self):
        return "savings are this way: "