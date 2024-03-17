import os
import time
from login import ClickupLogin
from scrapy_xlsx import ScrapyXlsx
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':

    current_dir = os.path.dirname(os.path.realpath(__file__))

    download_dir = os.path.join(current_dir, 'data\clickup_sheet_negocios')

    options = Options()
    prefs = {'download.default_directory': download_dir}
    options.add_experimental_option('prefs', prefs)
    # Instantiate the driver only once in the main
    driver = webdriver.Chrome(options=options)

    # Set the browser window size to 1300x900
    driver.set_window_size(1300, 900)

    # Instantiate the ClickupLogin class, passing the instantiated driver
    credentials = ClickupLogin(
        driver, 'vinicius.reis@tahto.com.br', '1a2b3c4dT!'
    )
    scrapy = ScrapyXlsx(driver)
    # Perform login
    credentials.login()
    time.sleep(4)
    scrapy.go_to_extract()
    time.sleep(4)
    # Check the presence of the element

    # Wait for a sufficient time before closing the browser
    time.sleep(200)  # 10 seconds of wait

    # Close the browser
    driver.quit()
