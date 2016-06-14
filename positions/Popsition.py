from datetime import datetime

from decimal import Decimal


class Position:

    TYPE_LONG = 'long'
    TYPE_SHORT = 'short'
    POSITION_TYPES = [TYPE_LONG, TYPE_SHORT]

    STATUS_OPEN = 'open'
    STATUS_CLOSED = 'closed'
    POSITION_STATUSES = [STATUS_OPEN,STATUS_CLOSED]

    def __init__(self, team, date, symbol, position_type, entry_price, quantity, cost, close_price, market_value, position_status, exit_date, open_profit, profit_percentage, net_value, invested):
        self.team = team
        self.date = datetime.strptime(date.strip(), "%m/%d/%Y")
        self.symbol = symbol
        self.position_type = position_type.lower()
        self.entry_price = self._makeDecimal(entry_price)
        self.quantity = int(str(quantity).translate(None, ',$'))
        self.cost = self._makeDecimal(cost)
        self.close_price = self._makeDecimal(close_price) if close_price else None
        self.market_value = self._makeDecimal(market_value) if market_value else None
        self.position_status = position_status
        self.exit_date = datetime.strptime(exit_date.strip(), "%m/%d/%Y") if exit_date else None
        self.profit_percentage = profit_percentage
        self.open_profit = self._makeDecimal(open_profit) if open_profit else None
        self.net_value = self._makeDecimal(net_value) if net_value else None
        self.invested = self._makeDecimal(invested) if invested else None

    def _makeDecimal(self, value):
        try:
            return Decimal(str(value).translate(None, '$,()\''))
        except:
            return None

    def __str__(self):
        return "%s\n" % self.__dict__

    def __repr__(self):
        return self.__str__()
