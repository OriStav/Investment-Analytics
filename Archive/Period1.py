import pandas as pd
import numpy as np
import yfinance as yf
from dateutil.relativedelta import relativedelta 


class Period():        
    def __init__(self,Stock):
        self.stocks_df=Stock.stocks_df   
        return self.nearest_index_by_stocks()
    def get_last_indices(self):
        return self.nearest_index_by_stocks(self.last_investment_date())
    def get_first_indices(self,last_investment):
        len_stock=self.stocks_df.groupby("symbol").apply(lambda x:max(x.index)-min(x.index)+1)
        zero_index=self.stocks_df.groupby("symbol").apply(lambda x:min(x.index))
        cut_len_stock=last_investment-zero_index+1
        diff_len=len_stock-cut_len_stock
        first_withdrawal=zero_index+diff_len
        return first_withdrawal
    def last_investment_date(self):
        by_last_withdrawl=self.yearsdelta(self.last_withdrawal+
                                        self.investment_duration,"-")
        last_investment_date=self.yearsdelta(self.investment_duration,"-")
        last_date=min(by_last_withdrawl,last_investment_date)
        return last_date                 
    # def nearest_index_by_stocks(self,target_date):    
    #     diff_days=(self.stocks_df.Date-target_date).dt.days
    #     diff_days_abs=np.abs(diff_days)
        
    #     temp_df=self.stocks_df[["symbol"]]
    #     temp_df["diff_days_abs"]=diff_days_abs
        
    #     stocks_index=temp_df.groupby("symbol")["diff_days_abs"].idxmin() 
        
    #     return stocks_index    
    @staticmethod
    def yearsdelta(years,math,from_date=None):
        from dateutil.relativedelta import relativedelta
        if from_date is None:
            from_date = pd.datetime.now()
        if math=="-":
            return from_date - relativedelta(years=years)
        elif math=="+":
            return from_date + relativedelta(years=years)
            
