import pandas as pd
import numpy as np
import yfinance as yf
from dateutil.relativedelta import relativedelta 

class Stock():   
    def __init__(self,symbols):
        self.stocks_df=pd.DataFrame()
        for symbol in symbols:
            stock = yf.download(symbol)
            stock["symbol"]=symbol
            self.stocks_df=pd.concat([ self.stocks_df, stock ])
        self.stocks_df=self.stocks_df.reset_index()
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
        
        transactions=pd.DataFrame({"CloseValueDelta":delta,
                                  "CloseValueDeltaPerc":delta_in_perc,
                                  "DurationDelta":dur})
        transactions=pd.concat([investment,withdrawal,transactions],axis=1)    
        transactions=transactions.dropna()
        return transactions
    #%%
    def analyze(self,id):
        self.last_investment=id.get_last_indices()
        self.first_withdrawal=id.get_first_indices(self.last_investment)
        self.last_withdrawal=id.get_last_withdrawal()
        stocks_grps=self.stocks_df.groupby("symbol")
        self.stocks_loop(stocks_grps)
    def stocks_loop(self,stocks_grps):
        self.stocks_delta=pd.DataFrame()
        for stock in stocks_grps:
            print(stock[0])            
            last_investment=self.last_investment[stock[0]]
            first_withdrawal=self.first_withdrawal[stock[0]]
            stock_delta=self.calc_deltas(stock[1], last_investment,first_withdrawal)
            self.stocks_delta=self.stocks_delta.append(stock_delta)
            sv=stock.loc[first_withdrawal:last_investment,["Date","Close"]]
            self.stocks_values=self.stocks_values.append()