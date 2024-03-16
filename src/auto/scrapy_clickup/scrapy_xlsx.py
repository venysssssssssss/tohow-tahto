import time

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ScrapyXlsx:
    def __init__(self, driver):
        self.driver = driver

    def go_to_extract(self):
        try:
            # Clicar no elemento //*[@id="cdk-drop-list-0"]/cdk-tree-node[4]/cu-project-row/cu-sidebar-row-layout/a/span/span
            self.driver.find_element(
                By.XPATH,
                '//*[@id="cdk-drop-list-0"]/cdk-tree-node[4]/cu-project-row/cu-sidebar-row-layout/a/span/span',
            ).click()

            time.sleep(2)

            # Clicar no elemento //*[@id="cu-data-view-item__link_4-49135222-1"]/div
            self.driver.find_element(
                By.XPATH, '//*[@id="cu-data-view-item__link_4-49135222-1"]/div'
            ).click()

            time.sleep(2)

            # Clicar no elemento //*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/div[1]/div[1]/div/button[2]
            self.driver.find_element(
                By.XPATH,
                '//*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/div[1]/div[1]/div/button[2]',
            ).click()

            time.sleep(2)

            # Clicar no elemento //*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/div[3]/div/cu-dropdown-list-item[5]/button/div/div/cu-export-view/div/div/div/div
            self.driver.find_element(
                By.XPATH,
                '//*[@id="app-root"]/cu-app-shell/cu-manager/div[1]/div/div/main/cu-dashboard/div/cu-views-bar-container/cu2-views-bar/div[3]/div/cu-dropdown-list-item[5]/button/div/div/cu-export-view/div/div/div/div',
            ).click()

            # Primeiro clique
            pyautogui.click(x=1026, y=270)
            time.sleep(2)

            # Segundo clique
            pyautogui.click(x=1027, y=370)
            time.sleep(2)

            # Terceiro clique
            pyautogui.click(x=1023, y=700)
            time.sleep(2)

            # Quarto clique
            pyautogui.click(x=1056, y=741)

            time.sleep(4)
        except Exception as e:
            print(f'An error occurred: {str(e)}')
