from biases_tests.BaseBias import BaseBias
from utils.PositionUtils import positions_to_dict_of_positions_by_symbol, sort_positions_by_date


class HotHandBiasMultipleBuys(BaseBias):

    def __init__(self, positions):
        self.hit_count = 0
        self.report_instances = []
        super(HotHandBiasMultipleBuys, self).__init__(positions)

    def test(self):
        positions_by_symbol = positions_to_dict_of_positions_by_symbol(self.positions)
        for symbol, positions in positions_by_symbol.iteritems():
            sort_positions_by_date(positions)
            last_exit = None
            max_buy_streak = 0
            current_buy_streak = 0
            for position in positions:
                if last_exit is None or position.date < last_exit:
                    current_buy_streak += 1
                else:
                    max_buy_streak = max(current_buy_streak, max_buy_streak)
                    current_buy_streak = 0
                last_exit = position.exit_date
            if max_buy_streak > 1:
                self.hit_count += 1
                self.report_instances.append("Found %d consecutive buys of stock symbol: %s" % (max_buy_streak, symbol))
        return self.hit_count > 0


    def getReport(self):
        return "\n".join(self.report_instances)


