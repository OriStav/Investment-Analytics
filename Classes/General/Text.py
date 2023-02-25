import inspect
from datetime import date
import time

class Text():
    def __init__(self):   
        self._tic_=time.perf_counter()

        self.symbols=f"symbols:"
        self.base=f"base path:"
        self.invst_dur=f"invst_dur:"
        self.lst_wthrwl=f"lst_wthrwl:"
        self.export_path=f"export path:"
        self.run_duration=f"run duration:"
        self.run_date=f"run date:"
        
        self.append(str(date.today()),"run_date")
    def replace(self,txt,category=None):
        txt= self.fix_txt(txt) 
        setattr(self,category,txt)
    def append(self,txt,category=None):
        txt= self.fix_txt(txt) 
        setattr(self,category, getattr(self, category)+"\n"+txt)
    def fix_txt(self,txt):
        #staticmethod - no decoration because of wrap method
        if type(txt)==list:
            txt=' '.join(txt)
        elif type(txt)==int:
            txt=str(txt)
        return txt    
    def wrap(self,location=None):
       toc=time.perf_counter()
       self.append(f"{toc-self._tic_:0.1f} seconds","run_duration")
       self. all_txt=""
       for i in inspect.getmembers(self):
            if not i[0].startswith('_'):
                if not inspect.ismethod(i[1]):
                    self.all_txt+=i[1]+"\n"
       if type(location) is str:
           with open(location,'a') as f:
                f.write(self.all_txt)
       return self.all_txt        
