from tkinter import Tk
from tkinter.filedialog import askopenfilename
from dataclass import Item, Template
from GS1Class import *
import pandas as pd

if __name__ == '__main__':
    print('Running...')
    

    
##    objs = Template()
##    for obj in objs:
##        page.create_new(obj)
##        page.download() # Need to make just download or actually combine
    page = Page()
    page.login()

## Make item then use the page.create_and_download(obj) method.
    

