from selenium.webdriver import Chrome,Edge
from selenium.webdriver.common.keys import Keys

def load_page(url):

    driverpath="Downloads//chromedriver.exe"
    
    browser=Chrome(executable_path=driverpath)
    browser.get(url)
    browser.find_elements_by_xpath('//*[@id="yfin-usr-qry"]').send_keys("VWAGY")
    browser.find_elements_by_xpath('//*[@id="header-desktop-search-button"]/svg').click()
    s=browser.page_source()
    print(s)
    #tt.send_keys(Keys.ENTER)
     # to refresh, next and back page
     
    #browser.refresh()
    #browser.back()
    #browser.forward()
    
    
    # maximize window, minimize window, restore window
    
    #browser.maximize_window()
    #browser.minimize_window()
    
    #x,c = browser.get_window_size().values()
    #browser.set_window_size(x,c)
load_page("https://finance.yahoo.com/")

