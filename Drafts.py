
#%%Drafts
# import matplotlib.dates as mdates

# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    #%%
# =============================================================================
#     def analyze(self,id):
#         self.last_investment=id.get_last_indices()
#         self.first_withdrawal=id.get_first_indices(self.last_investment)
#         self.last_withdrawal=id.get_last_withdrawal()
#         stocks_grps=self.stocks_df.groupby("symbol")
#         self.stocks_loop(stocks_grps)
# =============================================================================
# =============================================================================
# labels=['0-100','100-200','more than 200']
# a=transactions.groupby(pd.cut(transactions['CloseValueDeltaPerc'],
#                               bins=bins,
#                               labels=labels)).size().reset_index(name='count')
# =============================================================================
# def calc_deltas(stock,Details):    
    
#     investment_range=range(Details.loc["First",('Investment','ix')],
#                          Details.loc["Last",('Investment','ix')])
#     withdrawal_range=range(Details.loc["First",('Withdrawal','ix')],
#                          Details.loc["Last",('Withdrawal','ix')])
#     investment=stock.loc[investment_range,["Date","Close"]]
#     withdrawal=stock.loc[withdrawal_range,["Date","Close"]]
#     delta=withdrawal["Close"]-investment["Close"]
#     delta_in_perc=100*(delta/investment["Close"])
#     # dur=withdrawal.Date.reset_index()-investment.Date.reset_index()
#     dur=withdrawal.reset_index()["Date"]-investment.reset_index()["Date"]
#     # return withdrawal_range,delta,delta_in_perc,dur
#     return pd.DataFrame({"CloseValueDelta":delta,
#                           "CloseValueDeltaPerc":delta_in_perc,
#                           "DurationDelta":dur})


# def nearest_index(stock_date,target_date):    
#     diff_days=(stock_date-target_date).dt.days
#     diff_days_abs=np.abs(diff_days)        
#     return diff_days_abs.idxmin() 
# stock_date=Stock.stocks_df.loc[Stock.stocks_df.symbol=="AAPL","Date"]
# a=stock_date.loc[18314]+ relativedelta(days=2)
# b=nearest_index(stock_date,a)
# # 18314

# from dateutil.relativedelta import relativedelta 

# data = {'Withdrawal': ,
#            'Investment': ['Brussels', 'New Delhi', 'Brasília']}

# df = pd.DataFrame(data,
# columns=['Country', 'Capital', 'Population'])


# df = pd.DataFrame(np.random.rand(50,5))


# s=pd.Series(['Belgium', 'India', 'Brazil'])

# ndf=pd.concat([df,df],axis=1)
# print(f"size invested {self.invested.Close.size} ")
# print(f"size withdrawn {self.withdrawn.Close.size} ")
# sc=stock_comparison()
# #%Mockup
# sc.investment_duration=3#Years
# sc.end_history=3#Years Ago

# #%Main
# sc.download()

# #%%
# pl="+"
# z=eval("1"+pl+"2")

# #%% Delta Months example
# data=pd.DataFrame()
# data['start_date'] = pd.to_datetime(stock.index)
# data['end_date'] = pd.to_datetime(stock.index)+ np.timedelta64(1,'Y')

# stocks_grp=self.stock_df.groupby("symbol")

# a=sc.invested
# b=sc.withdrawn
    # def get_first_indices(self,from_date):
    #     first_withdrawal_date=self.yearsdelta(self.investment_duration,"+",from_date)
    #     return self.nearest_index_by_stocks(first_withdrawal_date)

# first_withdrawal=id.get_first_indices()
#%

# stocks=sc.stocks_df.groupby("symbol")
# a=stocks.get_group("AAPL")
# sz=sc.stocks_df.Date.size

    # first_withdrawal=id.get_first_indices(min(stock[1].Date))
    # first_withdrawal=last_investment[stock[0]]
# sz=sc.stocks_df.Date.size
# len_stock=sc.stocks_df.groupby("symbol").apply(lambda x:max(x.index)-min(x.index)+1)
# sm=len_stock.sum()
# a.index=a.index+9
# a1=a[a.index[1]]
# stocks_index_first=stocks_index_last

# a=sc.stock_df.loc[li["AAPL"],:]
# b=sc.stock_df.loc[li["^GSPC"],:]
# =============================================================================
# EVAL?
#     def loop_symbols():
#         for symbol in self.symbols:
#             _,analyzed=funcs.stock_analyze(stock,investment_duration)  
#             if 'analyzed_df' in locals():
#                 analyzed_df=pd.concat([ analyzed_df, analyzed ])
#             else:#first iteration
#                 analyzed_df=analyzed
# =============================================================================
# def samples_loop_backup(stock):
#     for sample in range(len(stock)-d):
#         invested=stock["Close"].take([sample])
#         withdrawn=stock["Close"].take([sample+d])
#         delta=withdrawn-invested
#         analyzed_per_year=100*(delta/invested)/365;

#https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python
#from yahoofinancials import YahooFinancials

#Series.equals
#Series.at_time(time)

#aapl_df['Close'].plot(title="APPLE's stock price")

# investment_duration=(stock.index.max()-stock.index.min()).days
# print(investment_duration)
# print(stock["Close"].take([1]))

# from dateutil.relativedelta import relativedelta 
# import pandas as pd


# def yearsago(years, from_date=None):
#     if from_date is None:
#         from_date = pd.datetime.now()
#     return from_date - relativedelta(years=years)


# a=pd.to_datetime(stock.index[1])+relativedelta(years=10)

# data['time_delta']=data['end_date']-data['start_date']

# data['time_delta_months'] = data['end_date'].dt.to_period('M').view(dtype='int64') -\
#     data['start_date'].dt.to_period('M').view(dtype='int64')
 
# print(data)

# def yearsago(years, from_date=None):
#     if from_date is None:
#         from_date = pd.datetime.now()
#     return from_date - relativedelta(years=years)

# text="stock: "+stock+"\n"+\
# "investment_duration: "+investment_duration+"\n"+\
#  "samples_per_day: "+samples_per_day

# investment_duration=(stock.index.max()-stock.index.min()).days/365
# samples_per_day=investment_duration/len(stock)

# symbol="^GSPC"
# stock = yf.download(symbol)
# stock["symbol"]=symbol
# #_,analyzed=funcs.stock_analyze(stock,investment_duration)

# investment_duration=(stock.index.max()-stock.index.min()).days
# print(investment_duration)
# print(stock["Close"].take([1]))

#############################


