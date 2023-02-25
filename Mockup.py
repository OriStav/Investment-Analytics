#%%
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
#%%
from Period import Period
from Stock import Stock
from Visual import Visual
#%%
from Text import Text
from Definition import Definition
from Path import Path
Def=Definition()
Path=Path(Def)
Text=Text()
# Def.text(Text)
# all_txt=Text.wrap()
df=Path.tree
#%%
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import table 

ax = plt.subplot(444, frame_on=False) # no visible frame

ax.xaxis.set_visible(False)  # hide the x axis
ax.yaxis.set_visible(False)  # hide the y axis

t=table(ax, df)  # where df is your data frame
plt.subplots_adjust(left=0.2, bottom=0.4) 
plt.savefig('mytable.png')
