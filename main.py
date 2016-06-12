import csv

from biases_tests.HotHandBiasMultipleBuys import HotHandBiasMultipleBuys
from biases_tests.LossAversionBias import LossAversionBias
from biases_tests.OptimismBias import OptimismBias
from positions.Popsition import Position

TestClasses = [HotHandBiasMultipleBuys, LossAversionBias, OptimismBias]
teams = dict()
with open('/Users/yossi/PycharmProjects/untitled/data/all_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        position = Position(**row)
        if not teams.get(position.team):
            teams[position.team] = []
        teams[position.team].append(position)

for team, positions in teams.iteritems():
    print "\nTeam: %s:" % team
    for TestClass in TestClasses:
        tester = TestClass(positions)
        print "Bias test: %s, Result: %s" % (tester.__class__.__name__, tester.test())
        print tester.getReport()
