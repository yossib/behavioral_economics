import csv

from biases_tests.AnchoringBiasDashboard import AnchoringBiasDashboard
from biases_tests.AnchoringBiasAri import AnchoringBiasAri
from positions.Popsition import Position

positions = []
TestClasses = [AnchoringBiasAri, AnchoringBiasDashboard]

with open('/Users/yossi/PycharmProjects/untitled/sheet1.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        positions.append(Position(**row))

for TestClass in TestClasses:
    tester = TestClass(positions)
    print "Test Bias %s, Result: %s" % (tester.__class__.__name__, tester.test())