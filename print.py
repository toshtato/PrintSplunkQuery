import time
import json
import os
from selenium import webdriver

search = input("enter string: ")

#driver = webdriver.Chrome('/home/tosh/chrome-selenium-python/chromedriver')  # Optional argument, if not specified will search path.

chrome_options = webdriver.ChromeOptions()
settings = {
    "appState": {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
}
prefs = {'printing.print_preview_sticky_settings': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/tosh/chrome-selenium-python/chromedriver')

driver.get('http://www.yahoo.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_id('header-search-input')
search_box.send_keys(search)
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.execute_script('window.print();')
driver.quit()

filename = (search)
os.rename('/home/tosh/Downloads/123 - Yahoo Search Results.pdf', (search)+'Logging.pdf')
