import datetime

from biases_tests.BaseBias import BaseBias
from utils.PositionUtils import positions_to_dict_of_positions_by_symbol, sort_positions_by_date
from yahoo_finance import Share

class OptimismBias(BaseBias):
    def __init__(self, positions):
        self.hit_count = 0
        self.report_instances = []
        super(OptimismBias, self).__init__(positions)

    def test(self):
        positions_by_symbol = positions_to_dict_of_positions_by_symbol(self.positions)
        for symbol, positions in positions_by_symbol.iteritems():
            sort_positions_by_date(positions)
            last_value = None
            first_position = None
            interesting_stocks = []
            for position in positions:
                if not last_value:
                    last_value = position.entry_price
                    first_position = position
                    continue
                if last_value > position.entry_price:
                    interesting_stocks.append((symbol, first_position, position))
                    first_position = position
                    last_value = position.entry_price
            for i, (symbol, first_position, other_position) in enumerate(interesting_stocks):
                try:
                    stock = Share(symbol)
                    dates = stock.get_historical((first_position.date + datetime.timedelta(weeks=-1)).strftime("%Y-%m-%d"),
                                                                   (other_position.date + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))
                    if len(dates) < 2:
                        print 'No historical info for symbol %s' % symbol
                        break
                    week_before, week_after = [dates[0], dates[-1]]
                    # print "testing optimism for symbol %s: comparing %s, %s, %s, %s" % (symbol, week_before['Adj_Close'], first_position.entry_price, other_position.entry_price, week_after['Adj_Close'])
                    if float(week_before['Adj_Close']) > float(first_position.entry_price) and float(other_position.entry_price) > float(week_after['Adj_Close']):
                        self.hit_count += 1
                        self.report_instances.append("Optimism found: 2 consqutive buys of symbol: %s while the stock has "
                                                     "benn going down for 4 weeks, prices: %s, %s, %s, %s" % (symbol, week_before['Adj_Close'], first_position.entry_price, other_position.entry_price, week_after['Adj_Close']))
                except Exception as e:
                    print "Unable to get historical data for stock %s, first date %s, last_date %s:" % (symbol,
                                                                                                        (first_position.date + datetime.timedelta(weeks=-1)).strftime("%Y-%m-%d"),
                                                                                                        (other_position.date + datetime.timedelta(weeks=1)).strftime("%Y-%m-%d"))
        return self.hit_count > 0

    def getReport(self):
        return "\n".join(self.report_instances)

