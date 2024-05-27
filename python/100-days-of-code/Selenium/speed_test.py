from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
    d = webdriver.Chrome(options=options)
    return d


driver = get_driver()
driver.get("https://www.speedtest.net/")
# <a href="#" role="button" tabindex="3"
# aria-label="start speed test - connection type multi"
# onclick="window.OOKLA.globals.shouldStartOnLoad = true;"
# class="js-start-test test-mode-multi">
#   <span class="start-ring"></span>
#   <span class="start-background"></span>
#   <span class="start-border"></span>
#   <span class="start-text">Go</span>
# </a>
webdriver.Chrome.implicitly_wait(driver, time_to_wait=0.2)
e = driver.find_element(By.CLASS_NAME, "js-start-test")
print(e)
e.click()
webdriver.Chrome.implicitly_wait(driver, time_to_wait=45.0)
try:
    # <a href="#" class="close-btn">Back to test results</a>
    e = driver.find_element(By.CLASS_NAME, "close-btn")
    e.click()
except:
    print("error finding and closing dialog")

try:
    xpath = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"
    e = driver.find_element(By.XPATH, xpath)
    print(f" download speed: {e.text}")
except:
    print('error using xpath')

try:
    # <span data-download-status-value="0.13" class="result-data-large number result-data-value download-speed">125.40</span>
    e = driver.find_element(By.CLASS_NAME, "download-speed")
    print( e.text)
except:
    print("error finding class name 'download-speed")

e = driver.find_element(By.CLASS_NAME, "upload-speed")
print( e.text)