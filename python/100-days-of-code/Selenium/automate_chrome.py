from selenium import webdriver
from selenium.webdriver.common.by import By


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument(
        f'--user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
    d = webdriver.Chrome(options=options)
    return d


def get_amazon_price(d: webdriver):
    url_gloves = "https://www.amazon.com/Getting-35117008151-Unlined-Buffalo-X-Large/dp/B004L13GAK"
    d.get(url_gloves)
    webdriver.Chrome.implicitly_wait(d, time_to_wait=1)
    # <span class="a-price-whole">21
    #     <span class="a-price-decimal">.</span>
    # </span>
    # <span class="a-price-fraction">20</span>
    #

    price = d.find_elements(By.CLASS_NAME, "a-price-whole")[0]
    price_cents = d.find_elements(By.CLASS_NAME, "a-price-fraction")[0]
    print(f"{price.text}.{price_cents.text}")


def scrape_python_org(d: webdriver):
    d.get("https://www.python.org/")
    search = d.find_elements(By.NAME, value="q")[0]
    print(search.get_attribute("placeholder"))
    button = d.find_elements(By.ID, value="submit")[0]
    print(button.size)


def using_xpath(driver: webdriver, path: str):
    # https://www.w3schools.com/xml/xpath_intro.asp
    driver.get("https://www.python.org/")
    e = driver.find_element(By.XPATH, path)
    print(e.text)


def get_upcoming_python_events(driver: webdriver):
    driver.get("https://www.python.org/")
    # <div class="medium-widget event-widget last">
    #    <div class="shrubbery">
    #        <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>
    #        <p class="give-me-more"><a href="/events/calendars/" title="More Events">More</a></p>
    #        <ul class="menu">
    #            <li>
    # <time datetime="2024-05-27T00:00:00+00:00"><span class="say-no-more">2024-</span>05-27</time>
    #  <a href="/events/python-events/1728/">GeoPython 2024</a></li>
    elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
    times = [e.get_attribute("datetime") for e in elements]
    elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
    names = [e.text for e in elements]
    events = {}
    for i in range(len(times)):
        events[i] = {
            "time": times[i],
            "name": names[i]
        }
    print(events)

def wikipedia_page_challenge(driver: webdriver):
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    e = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
    article_count = e.text
    print(article_count)

d = get_driver()
# get_amazon_price(d)
# scrape_python_org(d)
# using_xpath(d, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# get_upcoming_python_events(d)
wikipedia_page_challenge(d)

d.quit()  # exit Chrome
# driver.close() # close active tab
