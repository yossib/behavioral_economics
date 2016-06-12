from datetime import datetime

from biases_tests.BaseBias import BaseBias


class AnchoringBiasAri(BaseBias):
    suggested_stocks = ['AAPL','EBAY','AKAM','TWTR','T']

    def test(self):
        hit_count = 0
        total_positions = 0

        for position in self.positions:
            total_positions += 1
            if position.symbol in self.suggested_stocks and position.date.date() == datetime.strptime("4/11/2016", "%m/%d/%Y").date():
                hit_count += 1

        return float(total_positions) / float(hit_count) > 0.5 if hit_count > 0 else False