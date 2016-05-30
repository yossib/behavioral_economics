from datetime import datetime

from biases_tests.BaseBias import BaseBias


class AnchoringBiasAri(BaseBias):
    suggested_stocks = ['AAPL','EBAY','AKAM','TWTR','T']
    hit_count = 0

    def test(self):
        for position in self.positions:
            if position.symbol in self.suggested_stocks and position.date.date() == datetime.strptime("4/11/2016", "%m/%d/%Y").date():
                self.hit_count += 1
        return self.hit_count > 0