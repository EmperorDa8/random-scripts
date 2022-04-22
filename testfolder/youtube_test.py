from selenium.webdriver import Chrome,Edge
from selenium.webdriver.common.keys import Keys
import unittest
import HtmlTestRunner

class Youtube_Testing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        driverpath="C:\\Users\\USER\\Documents\\chromedriver.exe"
        cls.browser=Chrome(executable_path=driverpath)
        cls.browser.implicitly_wait(15)
    
    
    def testpart1(self):     
        self.browser.get("https://youtube.com")
        self.browser.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("halo")
        self.browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
        
        
    def testpart2(self):     
        self.browser.get("https://youtube.com")
        self.browser.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("python")
        self.browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
         
    def testpart3(self):     
        self.browser.get("https://youtube.com")
        self.browser.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("edureka")
        self.browser.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
        
   
        
    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.browser.quit()
        print("tests done successfully")
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/USER/testfolder"))