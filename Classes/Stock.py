import pandas as pd
import numpy as np
import yfinance as yf
from dateutil.relativedelta import relativedelta 

from Period import Period

class Stock():   
    def __init__(self,Def):
        self.stocks_df=pd.DataFrame()
        for symbol in Def.symbols:
            stock = yf.download(symbol)
            stock["symbol"]=symbol
            self.stocks_df=pd.concat([ self.stocks_df, stock ])
        self.stocks_df=self.stocks_df.reset_index()
        self.Period=Period(self.stocks_df,Def.invst_dur,Def.lst_wthrwl)        
        self.stocks_loop()
    def stocks_loop(self):
        stocks_grps=self.stocks_df.groupby("symbol")
        self.transactions=pd.DataFrame()
        for stock in stocks_grps:
            print(stock[0])                     
            # stock=Stock.stocks_df.loc[Stock.stocks_df.symbol=="AAPL",:]
            self.Period.fill_details(stock[0])
            transactions=self.calc_deltas(stock[1],self.Period.details)
            transactions["symbol"]=stock[0]
            self.transactions=pd.concat([self.transactions,
                                         transactions])
    def calc_deltas(self,stock,details):    

        investment_range=range(details.loc["First",('Investment','ix')],
                             details.loc["Last",('Investment','ix')])
        withdrawal_range=range(details.loc["First",('Withdrawal','ix')],
                             details.loc["Last",('Withdrawal','ix')])
        investment=stock.loc[investment_range,["Date","Close"]].reset_index()
        investment=investment.drop(columns="index")
        withdrawal=stock.loc[withdrawal_range,["Date","Close"]].reset_index()
        withdrawal=withdrawal.drop(columns="index")
        
        delta=withdrawal["Close"]-investment["Close"]
        delta_in_perc=100*(delta/investment["Close"])
        dur=withdrawal.reset_index()["Date"]-investment.reset_index()["Date"]
        
        transactions=pd.DataFrame({"Delta":delta,
                                  "DeltaPerc":delta_in_perc,
                                  "DurationDelta":dur})
        transactions=pd.concat([investment,withdrawal,transactions],axis=1)    
        transactions=transactions.dropna()
        return transactions