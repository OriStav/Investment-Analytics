class utilities:
    """
    This class is intended for use across all my codes,
    so it should always be in a folder contained in PYTHONPATH environment
    because it is also the class which adds temporary paths to the sys.path
    it is usually imported as
    Usage examples:
    >>>from utilities import utilities as util    
    >>>base="/Users/oristav/Library/CloudStorage/Dropbox/Library/Code/OriFin/#PyCode/Flow Analytics"
    >>>util().initializer(base)
    
    Improve by:
        make able to run on other pc - dynamic base path 
    """
    def __init__(self):
        pass
    @staticmethod
    def initializer(base,local_general_classes=False):
        """
        can return util this way if necessary for further developments:
            util=utilities.clc_clear()
            utilities.pather(base)
            return util
        """
        utilities.clc_clear()
        utilities.pather(base,local_general_classes)
        return base

    @staticmethod
    def clc_clear():
        """
        Example
        -------
        >>>util=util.clc_clear()

        Returns
        -------
        util
        (because it deletes it)

        """
        from IPython import get_ipython
        get_ipython().magic('clear')
        # get_ipython().magic('reset -sf')   
        
        get_ipython().magic('reset_selective -f ^(?!main$).*$')
        from utilities import utilities as util
        return util
    @staticmethod    
    def pather(base,local_general_classes):
        """
        Example
        -------
        >>>util.pather(""/Users/oristav/Library/CloudStorage/Dropbox/Library/Code/OriFin/#PyCode/Flow Analytics"")
        Parameters
        ----------
        base : TYPE, string
            to view updated system path:
            >>>from pprint import pprint
            >>>pprint(sys.path)
            
        Returns
        -------
        None.
        
        
        Improve
        -------
        Automatically check if there are "/Classes" and "/Classes/General" exist
        # from pprint import pprint
        # pprint(sys.path)

        """
        import sys
        import os
        os.chdir(base)
        sys.path.append(base+"/Classes")
        
        if local_general_classes:
            shared_classes_path='/Users/oristav/Library/CloudStorage/Dropbox/Library/Code/SharedClasses'
            if (shared_classes_path in sys.path):
                sys.path.remove(shared_classes_path)
            sys.path.append(base+"/Classes/General")
        


        
        