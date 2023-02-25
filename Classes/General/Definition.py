import inspect
class Definition():
    def __init__(self,Text,base):
        self.symbols=["^GSPC","AAPL","NFLX"]
        self.invst_dur=5#Years
        self.lst_wthrwl=0#Years Ago
        
        self.base=base;
        # "/Users/oristav/Library/CloudStorage"+\
        # "/Dropbox/Library/Code/OriFin"
        self.write(Text)
    def write(self,Text):
        for i in inspect.getmembers(self):
             if not i[0].startswith('_'):
                 if not inspect.ismethod(i[1]):
                     Text.append(i[1],i[0])