from config import GS1_USER, GS1_PASS, GS1_URL, BINARY_LOC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os
import time



class Page:

    def __init__(self):
        chrome_options = Options()
        chrome_options.headless = False
        chrome_options.binary_location = BINARY_LOC

        self.driver = webdriver.Chrome(os.path.abspath('chromedriver'),
                                       options=chrome_options)
        self.driver.implicitly_wait(10)

        # can we add the chrome_options here?
    def quit(self):
        return self.driver.quit()

    def login(self):
        driver = self.driver
        driver.get(GS1_URL)
        driver.find_element_by_xpath(
            '//input[@id="signInName"]').send_keys(GS1_USER)
        driver.find_element_by_xpath(
            '//input[@id="password"]').send_keys(GS1_PASS)

        driver.find_element_by_xpath(
            '//button[@id="next"]').click()
        # lands on 'Products' page
        driver.find_element_by_xpath(
            '//*[@id="product"]/a').click()
        return print('Logged in...')

    def create_new(self, obj):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="addnewproduct"]/a').click()
        # Single pass of GS1 creation loop.
        de = driver.find_element_by_xpath('//input[@id="txtProductDescription"]')
        de.send_keys(obj.name)
        # Brand Name
        bn = driver.find_element_by_xpath('//input[@id="txtBrandName"]')
        bn.send_keys(obj.brand_name)
        # SKU
        sku = driver.find_element_by_xpath('//input[@id="txtSKU"]')
        sku.send_keys(obj.sku)
        # Need to save here
        driver.find_element_by_xpath('//button[@id="btnSave"]').click()
        #Waits for the auto assign to pop up, clicks it and then moves to the continue model.
        time.sleep(1)
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="btnAutoAssign"]'))
         ).click()
        driver.find_element_by_xpath('//button[@id="btnAutoAssignGtinStartContinue"]').click()
        
##        # Save right here.
##        time.sleep(1)
##        elementd = WebDriverWait(driver, 10).until(
##            EC.element_to_be_clickable((By.XPATH, '//button[@id="btnSave"]'))
##         )
##        elementd.click()
####        driver.find_element_by_xpath('//button[@id="btnSave"]').click()
##        # Try to find status dropdown and change
        try:
            time.sleep(3)
            dropdown = Select(driver.find_element_by_xpath('//select[@id="ddlStatus"]'))
            dropdown.select_by_visible_text("In Use")

            # Save again.
            driver.find_element_by_xpath('//button[@id="btnSave"]').click()
            # asks for continue if marked 'In Use'
            try:
                driver.find_element_by_xpath('//button[@id="btnConfirmInUse"]').click()
            except:
                print('failed')

        except Exception as err:
            print(err)
            driver.find_element_by_xpath('//button[@id="btnSave"]').click()
            print('Item saved as Draft.')
            pass

    def download(self):
        driver = self.driver
        # Currently only starts from download point
        # Move on to barcode
        driver.find_element_by_xpath(
            '//*[@id="ProductdetailTabs"]/li[6]/a').click()
        
        # Attempts to wait for the 'preview' button.
        time.sleep(1)
        driver.find_element_by_xpath(
            '//button[@id="btnPreview"]').click()
        # downloads preview PNG
        driver.find_element_by_xpath(
            '//button[@id="btnDownload"]').click()
        upc = driver.find_element_by_xpath('/html/body/main/div/div[1]/div[1]/div/div/h1').text
        self.upc = upc.split(' ')[2][3:-1]
        print(f'Downloading png for {self.upc}')

        # closes
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="barcodePreviewModal"]/div[2]/div[1]/div[1]').click()
        print('download button clicked...')
        # returns the UPC into the object.
        return self.upc

    def find_existing(self):
        driver = self.driver
        driver.find_element_by_xpath(
            '//*[@id="dtProductList"]/tbody/tr[1]/td[3]/a').click()

        pass
    def create_and_download(self, obj):
        self.create_new(self, obj)
        self.download()

        return


