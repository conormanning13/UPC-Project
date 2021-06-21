from tkinter import Tk
from tkinter.filedialog import askopenfilename
from dataclass import Item, Template
from GS1Class import *

if __name__ == '__main__':
    print('Running...')
    
    def create_upc(item):
        page.create_new(item)
        page.download()
        return item.sku
    
##    objs = Template()
##    for obj in objs:
##        page.create_new(obj)
##        page.download() # Need to make just download or actually combine
    page = Page()
    page.login()
    page.create_new(i1)
##    page.find_existing()
    page.download()
##
##    print(objs)

