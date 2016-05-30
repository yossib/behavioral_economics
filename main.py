import csv

from biases_tests.AnchoringBiasDashboard import AnchoringBiasDashboard
from biases_tests.AnchoringBiasAri import AnchoringBiasAri
from positions.Popsition import Position

TestClasses = [AnchoringBiasAri, AnchoringBiasDashboard]
teams = dict()
with open('/Users/yossi/PycharmProjects/untitled/data/all_data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        position = Position(**row)
        if not teams.get(position.team):
            teams[position.team] = []
        teams[position.team].append(position)

for team, positions in teams.iteritems():
    for TestClass in TestClasses:
        tester = TestClass(positions)
        print "Team: %s, Test for Bias: %s, Result: %s" % (team, tester.__class__.__name__, tester.test())