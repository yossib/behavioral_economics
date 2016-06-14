import csv

from biases_tests.HotHandBiasMultipleBuys import HotHandBiasMultipleBuys
from biases_tests.LossAversionBias import LossAversionBias
from biases_tests.OptimismBias import OptimismBias
from positions.Popsition import Position
from utils.PositionUtils import sort_positions_by_date, positions_to_dict_of_positions_by_symbol, remove_shorts

TestClasses = [HotHandBiasMultipleBuys, LossAversionBias, OptimismBias]
teams = dict()
with open('/Users/yossi/PycharmProjects/untitled/data/data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        position = Position(**row)
        if not teams.get(position.team):
            teams[position.team] = []
        teams[position.team].append(position)

for team, positions in teams.iteritems():
    positions = remove_shorts(positions)
    print "\nTeam: %s:" % team
    for TestClass in TestClasses:
        tester = TestClass(positions)
        print "Bias test: %s, Result: %s" % (tester.__class__.__name__, tester.test())
        print tester.getReport()
    # for symbol, _positions in positions_to_dict_of_positions_by_symbol(positions).iteritems():
    #     print "Positions for Symbol: %s\n" % symbol
    #     sort_positions_by_date(_positions)
    #     print _positions
    #     print "\n\n"
