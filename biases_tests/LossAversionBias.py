from biases_tests.BaseBias import BaseBias
import numpy as np

class LossAversionBias(BaseBias):
    def __init__(self, positions):
        self.report = ""
        super(LossAversionBias, self).__init__(positions)

    def test(self):
        loss_positions_count = 0
        profit_positions_count = 0
        time_in_profit_positions = 0
        time_in_loss_positions = 0
        for position in self.positions:
            if position.exit_date:
                time_in_position = (position.exit_date-position.date).total_seconds()
                if position.entry_price > position.close_price:
                    loss_positions_count += 1
                    time_in_loss_positions += time_in_position
                else:
                    profit_positions_count +=1
                    time_in_profit_positions += time_in_position
        result = ((float(time_in_loss_positions) / float(loss_positions_count)) <
               (float(time_in_profit_positions) / float(profit_positions_count))) if profit_positions_count > 0 and loss_positions_count > 0 else False

        if result:
            resolution = 0.01
            avg_time_in_loss = (float(time_in_loss_positions) / float(loss_positions_count) / (60*60*23))
            avg_time_in_profit = (float(time_in_profit_positions) / float(profit_positions_count) / (60*60*24))

            avg_time_in_loss = int(np.round(avg_time_in_loss / resolution)) * resolution
            avg_time_in_profit = int(np.round(avg_time_in_profit / resolution)) * resolution
            self.report = "Average hold in losing positions is: %s days versus %s days in profit positions" % \
                          (avg_time_in_loss, avg_time_in_profit)
        return result

    def getReport(self):
        return self.report