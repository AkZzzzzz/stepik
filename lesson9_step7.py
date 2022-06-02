from selenium import webdriver
import time
import math
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID,"price"), "100")) 
    browser.find_element(by='id', value='book').click()
  
    x_element = browser.find_element(by='id',value='input_value')
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    
    input = browser.find_element(by='id',value='answer')
    input.send_keys(y)
        
    button = browser.find_element(by='id', value='solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:

    time.sleep(10)

    browser.quit()

