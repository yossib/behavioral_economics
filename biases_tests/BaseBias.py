class BaseBias(object):

    def __init__(self, positions):
        self.positions = positions

    def test(self):
        raise NotImplementedError()

    def getReport(self):
        raise NotImplemented()
