# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import logging
import time
import winsound

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def run_selenium(name):
    # Use a breakpoint in the code line below to debug your script.
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Edge()
    driver.get("https://web.whatsapp.com")
    # assert "Python" in driver.title
    # elem = driver.find_element("q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    # driver.close()
    while True:
        try:
            element = WebDriverWait(driver, 10).until(
                lambda x: x.find_element(
                    By.XPATH,
                    '/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/header/div[2]/div[2]/span'
                )
            )
            assert isinstance(element, WebElement)
            if element.text == 'online':
                now = datetime.datetime.now()
                s = now.strftime('%A %d/%B %H:%M:%S')
                print(s)
                with open('online.txt', 'a') as f:
                    f.write('%s\n' % s)
        except (TimeoutException, StaleElementReferenceException) as e:
            logger.warning(e)
        time.sleep(1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_selenium('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
