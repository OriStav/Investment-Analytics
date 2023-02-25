import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale


class Visual():
    def __init__(self,Stock):
        Stock.transactions.columns=["Investment Date","Investment Close",
                    "Withdrawal Date","Withdrawal Close",
                    "Delta","DeltaPerc","DurationDelta","Symbol"]
        self.transactions=Stock.transactions
        self.all_details=Stock.Period.all_details
    def tables(self):
        transactions_stats=self.transactions[["DeltaPerc",
                                          "DurationDelta"]].describe()
        transactions_min_max=pd.concat([self.transactions.min(),
                                        self.transactions.max()],axis=1)
        all_details=self.all_details        
        return (transactions_stats ,transactions_min_max ,all_details)
    def make_bins(self):
        bins = [-np.inf,0,15,30,np.inf]
        bins=self.transactions.groupby\
            ([pd.cut(self.transactions['DeltaPerc'],
            bins=bins),"Symbol"]).size().reset_index(name='count')
        bins["Probability"]=round(100*bins["count"]/sum(bins["count"]),0)
        self.bins=bins.sort_values(by="Probability",ascending=False)
        return self.bins
    def plot_bars(self):
        self.make_bins()
        table = pd.pivot_table(self.bins, values='Probability',
                               index="DeltaPerc",
                           columns=['Symbol'])
        ax = table.plot.bar(rot=0)
        for container in ax.containers:
            ax.bar_label(container)
        ax.set_ylabel('Probability [% of samples]')
        ax.set_xlabel('Revenue: Delta/Invested [%]')
        ax.set_title('Average Periodical Revenue')
    def plot_box(self):
        delta_perc_by_symbol = self.transactions.pivot(values='DeltaPerc',
                                columns=['Symbol'])
        ax = delta_perc_by_symbol.boxplot(rot=0)
        ax.set_ylabel('Revenue: Delta/Invested [%]')
        ax.set_title('Average Periodical Revenue Box Distribution')
    def plot_timeline(self,norm,transactions_column):
        delta_perc_by_symbol = self.transactions.pivot(\
                                   values=transactions_column,columns=['Symbol'])
        dates_by_symbol = self.transactions.pivot(\
                          values='Investment Date', columns=['Symbol'])
        
        for symbol in dates_by_symbol.columns:
            x1=dates_by_symbol[symbol].dropna()
            if norm=="Normalized" or norm=="xNormalized" :
                x1 = minmax_scale(x1)

            y1= delta_perc_by_symbol[symbol].dropna()# many thanks to Kyss Tao for setting me straight here
            if norm=="Normalized" or norm=="yNormalized":
                y1 = minmax_scale(y1)
                
            plt.plot(x1,y1,label=symbol)
        plt.legend()
        plt.title(transactions_column+" Value Vs Date")
        plt.ylabel(transactions_column+" "+norm)
        plt.xlabel('Date')
    @staticmethod
    def open_file(path):
        import os
        import platform
        import subprocess
        
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
        
    