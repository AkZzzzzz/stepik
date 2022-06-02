from selenium import webdriver
import time
import math
from selenium.webdriver import ChromeOptions

link = "http://suninjuly.github.io/execute_script.html"

try:
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.get(link)
    
    x_element = browser.find_element(by='id',value='input_value')
    x = x_element.text
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    

    input = browser.find_element(by='id',value='answer')
    print(input)
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
    input.send_keys(y)
    
    option1 = browser.find_element(by='id',value='robotCheckbox')
    option1.click()
    
    option2 = browser.find_element(by='id',value='robotsRule')
    option2.click()
        
    button = browser.find_element(by='class name', value='btn-primary')
    button.click()

finally:

    time.sleep(10)

    browser.quit()

