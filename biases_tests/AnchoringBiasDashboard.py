from biases_tests.BaseBias import BaseBias


class AnchoringBiasDashboard(BaseBias):
    suggested_stocks = ['CLR','CRK(F)','CVX','CWEI','DK','DNR','HES','NBL','NE','NOV','PQ(F)','SE','SM','SU','USO','VLO','WLL','WTI','XCO','XEC','XLE','XOM','XOP','LNG','UNG','ASTI(D,F)','CSIQ','FSLR','JASO','JKS','SCTY','SOL','SPWR','TSL','TSL','YGE','DRYS','DSX','EGLE(F)','ESEA','KEX','NM','PRGN','SB(F)','SBLK(F)','FREE','BYDDY(D)','F','GM','TSLA','FDX','UPS','WU','CME','XLF','SKF','GS','DB','JPM','MS','BCS','C','ZION','BAC','CS','WFC','USB','UBS','RBS','TD','HSBC','RF','KEY','AMTD','SCHW','ETFC','IBKR','EZPW','NDAQ','V','MA','AXP','COF','WU',' ','LVS','HLT','WYNN','SGMS','BYD','MGM','MCRI','ISLE','PENN','MAR','HOT','X','AA','MT','AP','GGB','GSI(H)','MTL','NUE','TS','SID','CBI','RIO','BHP','DGP','UGL','GDX','GLD','GOLD','ABX','GG','GFI','EFU','SDD','TWM','FXP','RGLD','AEM',' ','MON','MOS','POT','IPI','SQM','AGU',' ','DFT','DOW','PHM',' ','PFE','TEVA','BMY','GSK','MRK','AMGN','PRGO','MCD','WEN','DPZ','SBUX','PEP','KO','PBPB','BWLD','TSN','CPB','CMG','KKD',' ','XLY','BBY','JCP','M','SHLD','WMT','KSS','JWN','LB','TJX','ROST','VFC','ATVI','ANF','ZQK','GPS','COH','KORS','LULU','NKE','CROX','DWA','DIS','MPEL','P','TWX','AMC','EXPE','YELP','TRIP','PCLN']
    hit_count = 0

    def test(self):
        for position in self.positions:
            if position.symbol in self.suggested_stocks:
                self.hit_count += 1
        return self.hit_count > 0