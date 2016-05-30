from datetime import datetime

from decimal import Decimal


class Position:

    TYPE_LONG = 'long'
    TYPE_SHORT = 'short'
    POSITION_TYPES = [TYPE_LONG, TYPE_SHORT]

    STATUS_OPEN = 'open'
    STATUS_CLOSED = 'closed'
    POSITION_STATUSES = [STATUS_OPEN,STATUS_CLOSED]

    def __init__(self, date, symbol, position_type, entry_price, quantity, cost, close_price, market_value, position_status, exit_date, open_profit, profit_percentage, net_value, invested):
        self.date = datetime.strptime(date, "%m/%d/%Y")
        self.symbol = symbol
        self.position_type = position_type
        self.entry_price = self._makeDecimal(entry_price)
        self.quantity = int(quantity.replace(',',''))
        self.cost = self._makeDecimal(cost)
        self.close_price = self._makeDecimal(close_price)
        self.market_value = self._makeDecimal(market_value)
        self.position_status = position_status
        self.exit_date = datetime.strptime(exit_date, "%m/%d/%Y")
        self.profit_percentage = profit_percentage
        self.open_profit = self._makeDecimal(open_profit)
        self.net_value = self._makeDecimal(net_value)
        self.invested = self._makeDecimal(invested)

    def _makeDecimal(self, value):
        return Decimal(str(value).translate(None, '$,'))