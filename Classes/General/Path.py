import os
import pandas as pd

class Path():
    def __init__(self,Def):
        self.slash="/"
        if not(os.path.exists(Def.base+self.slash)):
            print("error: no path")
        self.tree= pd.DataFrame({"path":Def.base},index=["Base"])
        self.append("Visual","")
    def append(self,name,path):
        fullpath=self.tree.path[0]+self.slash+path
        self.tree.loc[name,"path"]=fullpath
        #%%     
    def find_files(self):
        files_folder=self.tree.path.tail(1).to_string(index=False)
        pkl_list=self.content_lister(files_folder,".pkl")
        xlsx_list=self.content_lister(files_folder,".xlsx")
        
        print(pkl_list)
        print(xlsx_list)
        return pkl_list  
    def content_lister(self,dir_path,suffix=".xlsx"):
        dir_list = os.listdir(dir_path)
        if suffix=="folder":
            contents_list= [val for val in dir_list if "." not in val]
        else:
            contents_list= [val for val in dir_list
                            if val.endswith(suffix)]
            contents_list= [val for val in contents_list
                            if not(val.startswith("~$"))]           
        return pd.Series(contents_list)
    