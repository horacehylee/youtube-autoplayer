"""
Webdriver script to get youtube urls and navigate through "Up next"
"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

def youtube_navigate(start_url, total=10, delay=5):
    "Navigate through youtube with 'Up next'"

    # xPath = "//div[@class='autoplay-bar']/div[@class='watch-sidebar-body']"
    xPath = "//a[@class='yt-simple-endpoint style-scope ytd-compact-video-renderer']"
    # xPath = "//ul[@class='video-list']"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--mute-audio")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver = webdriver.PhantomJS()

    driver.implicitly_wait(delay)

    youtube_urls = []

    try:
        driver.get(start_url)
        for _ in range(total):

            # youtube_urls.append((driver.title, driver.current_url))
            current_url = driver.current_url
            print(current_url)
            youtube_urls.append(current_url)

            element = driver.find_element_by_xpath(xPath)
            try:
                element.click()
            except StaleElementReferenceException:
                element = driver.find_element_by_xpath(xPath)
                element.click()

            # driver.save_screenshot("test" + str(i) + ".png")
            time.sleep(1)

    except NoSuchElementException:
        print("No such element, maybe the page is not loaded")
    except:
        print("Unexpected error:", sys.exc_info()[0])
    driver.close()
    return youtube_urls


def wait(driver, id, delay=10):
    "Wait until element id appears"
    try:
        element = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.ID, id))
        )
        return element
    except TimeoutException:
        print("Loading took too much time!")
        driver.close()
        raise
