from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
    d = webdriver.Chrome(options=options)
    return d
def get_amazon_price(d:webdriver):
    url_gloves = "https://www.amazon.com/Getting-35117008151-Unlined-Buffalo-X-Large/dp/B004L13GAK"
    d.get(url_gloves)
    webdriver.Chrome.implicitly_wait(d,time_to_wait=1)
    # <span class="a-price-whole">21
    #     <span class="a-price-decimal">.</span>
    # </span>
    # <span class="a-price-fraction">20</span>
    #

    price = d.find_elements(By.CLASS_NAME, "a-price-whole")[0]
    price_cents = d.find_elements(By.CLASS_NAME, "a-price-fraction")[0]
    print(f"{price.text}.{price_cents.text  }")


def scrape_python_org(d:webdriver):
   d.get("https://www.python.org/")
   search = d.find_elements(By.NAME,value="q")[0]
   print(search.get_attribute("placeholder"))
   button = d.find_elements(By.ID,value="submit")[0]
   print(button.size)


d= get_driver()
#get_amazon_price(d)
scrape_python_org(d)

d.quit()  # exit Chrome
# driver.close() # close active tab