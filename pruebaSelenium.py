from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "WINDOWS")
driver = webdriver.Remote(
     command_executor='https://'+ 'martnmiranda_nBdHPX' + ':' + 'kiyXF1ubqhXmAhBsidzT' + '@hub-cloud.browserstack.com/wd/hub',
    options=chrome_options
)
driver.get("https://selenium-tp.herokuapp.com/")
driver.quit()  