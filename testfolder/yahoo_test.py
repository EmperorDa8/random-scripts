from selenium.webdriver import Chrome,Edge
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner


class Yahoofinance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driverpath="C:\\Users\\USER\\Documents\\chromedriver.exe" 
        cls.browser=Chrome(executable_path=driverpath)
        cls.browser.implicitly_wait(5)    
    
    
    def test_yahoo(self):
        self.browser.get("https://finance.yahoo.com/")
        # to find items on the search bar using xpath and enter key
        self.browser.find_element_by_xpath('//*[@id="yfin-usr-qry"]').send_keys("NFT")
        self.browser.find_element_by_xpath('//*[@id="header-desktop-search-button"]').click()
        # to print the page source
        
    
    def test_yahoo2(self):
        self.browser.get("https://finance.yahoo.com/")
        # to find items on the search bar using xpath and enter key
        self.browser.find_element_by_xpath('//*[@id="yfin-usr-qry"]').send_keys("ETH")
        self.browser.find_element_by_xpath('//*[@id="header-desktop-search-button"]').click()
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("tests completed!")
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="c:/Users/USER/testfolder"))