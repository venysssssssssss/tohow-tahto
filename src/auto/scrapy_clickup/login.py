import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ClickupLogin:
    def __init__(self, driver, username, password):
        self.username = username
        self.password = password
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        try:
            # Acesse a página de login do Clickup
            self.driver.get('https://app.clickup.com/login')

            # Aguarde até que o campo de entrada de usuário/email esteja visível e interagível
            username_input = self.wait.until(
                EC.element_to_be_clickable((By.ID, 'login-email-input'))
            )

            # Envie o dado de login
            username_input.send_keys(self.username)

            # Encontre o campo de senha e insira a senha
            password_input = self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, 'login-password-input')
                )
            )
            password_input.send_keys(self.password)

            # Clique no botão de login
            self.driver.find_element(
                By.XPATH,
                '//*[@id="app-root"]/cu-login/div/div[2]/div[2]/div[1]/cu-login-form/div/form/button',
            ).click()

            time.sleep(4)

        except Exception as e:
            print(f'Ocorreu um erro: {e}')

    def check_element(self, xpath):
        try:
            elements = self.driver.find_elements(By.XPATH, xpath)
            if elements:
                return 'Presente'
            else:
                return 'Não está presente'
        except Exception as e:
            return f'Ocorreu um erro: {e}'
