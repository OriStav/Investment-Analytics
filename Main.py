#Refresh kernel first
def main(base):
    from Definition import Definition
    from Path import Path
    from Text import Text
    from Stock import Stock
    from Visual import Visual
    from Report import Report
    
    Text=Text()#tic
    Def=Definition(Text,base)
    Path=Path(Def)
    Stock=Stock(Def)
    Visual=Visual(Stock)
    Report=Report(Visual,Path,Text)#toc
    Report.save()
    Visual.open_file(Path.tree.path["Visual"])


if __name__ == '__main__':
    from utilities import utilities as util    
    base="/Users/oristav/Library/CloudStorage/Dropbox/Library/Code/OriFin/#PyCode/Investment Analytics"
    # base="/Users/oristav/Dropbox/Library/Code/OriFin/#PyCode/Investment Analytics"
    base=util().initializer(base,True)
    a=main(base)

#%%

#%%TODO
#add tables to report - from Visual.tables and mockup code
#add import cleaning_excels for stocks groups