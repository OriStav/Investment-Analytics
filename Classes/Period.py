import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta 


class Period():            
    def __init__(self,stocks_df,invst_dur,lst_wthrwl):
        x = [('Stock','Symbol'),
            ('Withdrawal','years-ago'),('Withdrawal','date'),('Withdrawal','ix'),
             ('Investment','years-ago'),('Investment','date'),('Investment','ix')]
        self.col_list = pd.MultiIndex.from_tuples(x)
        self.stocks_df=stocks_df
        self.invst_dur=invst_dur
        self.lst_wthrwl=lst_wthrwl
        self.all_details=pd.DataFrame()
    def fill_details(self,symbol):
        self.details= pd.DataFrame(np.full([2, 7], np.nan),
                                   ["First","Last"],self.col_list)
        self.details.columns.names=['Action','State']
        
        self.details.iloc[:,0]=symbol
        self.stock_date=self.stocks_df.loc[self.stocks_df.symbol==symbol,"Date"]
        self.get_yearsago()
        self.get_dates()
        # self.get_closest()
        self.get_indices()
        self.all_details=pd.concat([self.all_details,self.details])
    def get_yearsago(self):
        self.details.loc["First",
                     ('Investment','years-ago')]=\
        round((datetime.today().date()-min(self.stock_date).date()).days/365)
        self.details.loc["Last",
                     ('Investment','years-ago')]=self.invst_dur+self.lst_wthrwl
        self.details.loc["First",
                     ('Withdrawal','years-ago')]=\
        self.details.loc["First",('Investment','years-ago')]-self.invst_dur
        self.details.loc["Last",('Withdrawal','years-ago')]=self.lst_wthrwl
    def get_dates(self):
        dates=self.details.applymap(lambda x:self.yearsdelta(x, "-"))
        self.details.iloc[:,[2,5]]=dates.iloc[:,[1,4]] 
        self.details.loc["First",
                      ('Investment','date')]=min(self.stock_date)
        self.details.loc["First",
                      ('Withdrawal','date')]=\
                        self.yearsdelta(self.invst_dur,
                                        "+",min(self.stock_date))
    @staticmethod
    def yearsdelta(years,math,from_date=None):
        if pd.notnull(years) and type(years) is not str:       
            if from_date is None:
                from_date = datetime.today()
            if math=="-":
                return from_date - relativedelta(years=years)
            elif math=="+":
                return from_date + relativedelta(years=years)
    def get_indices(self):
        indices=self.details.applymap(lambda x:self.nearest_index(x))
        self.details.iloc[:,[3,6]]=indices.iloc[:,[2,5]]
    def get_closest(self):
        indices=self.details.applymap(lambda x:self.nearest_date(x))
        self.details.iloc[:,[3,6]]=indices.iloc[:,[2,5]]
    def nearest_date(self,target_date):
        if  type(target_date) is pd._libs.tslibs.timestamps.Timestamp: 
            diff_days=(self.stock_date-target_date).dt.days
            diff_days_abs=np.abs(diff_days)     
            return self.stock_date.loc[diff_days_abs.idxmin()]
    def nearest_index(self,target_date):
        if  type(target_date) is pd._libs.tslibs.timestamps.Timestamp: 
            diff_days=(self.stock_date-target_date).dt.days
            diff_days_abs=np.abs(diff_days)     
            return diff_days_abs.idxmin() 