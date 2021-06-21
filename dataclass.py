import pandas as pd
import re
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from config import GS1_BRAND_NAME

# Takes rows from dataframe on init and makes objects with callable sku, name
'''
Need to make Template item have Len and make subscriptable.
Also come up with a better fucking name.
'''

     return f'{self.sku} - {self.name}'

class Item:
    def __init__(self, SKU, Name):
        self.sku = SKU
        self.name = Name
        self.brand_name = GS1_BRAND_NAME
        self.UPC = None
        self.RetilPrice = 1
        self.Cost = 1

    def __repr__(self):
        return f'{self.sku} - {self.name}'

# Takes path, makes pandas dataframe, and prepares for GS1
class Template:
    def __init__(self):
##        print('Opening system file dialog.')
##        Tk().withdraw()
##        filepath = askopenfilename()
##        print('Template initialized from file.')

##        self.path = filepath
        self.df = pd.read_clipboard(dtype=str)
        self.objs = [Item(row) for row in self.df.iterrows()]

    # Makes items iterrable so that GS1 script can be called.
    def __iter__(self):
        return iter(self.objs)

    def __repr__(self):
        for obj in self.objs:
            print(obj)
        return f'{len(self.objs)} items detected'

    def __getitem__(self, i):
        return self.objs[i]
